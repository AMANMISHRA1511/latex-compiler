# compiler\views.py

import os
import subprocess
import tempfile
import base64
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt # Disable CSRF protection for this specific API endpoint
@require_POST
def compile_latex(request):
    try:
        # 1. Get LaTeX code from the request
        data = json.loads(request.body)
        latex_code = data.get('code')
        if not latex_code:
            return JsonResponse({'success': False, 'log': 'No LaTeX code provided.'}, status=400)

        # 2. Create a temporary directory to store files
        with tempfile.TemporaryDirectory() as temp_dir:
            tex_file_path = os.path.join(temp_dir, 'main.tex')
            pdf_file_path = os.path.join(temp_dir, 'main.pdf')
            docx_file_path = os.path.join(temp_dir, 'main.docx')
            log_file_path = os.path.join(temp_dir, 'main.log')

            # 3. Write the LaTeX code to a .tex file
            with open(tex_file_path, 'w', encoding='utf-8') as f:
                f.write(latex_code)

            # 4. Execute pdflatex
            pdflatex_command = [
                'pdflatex',
                '-interaction=nonstopmode',
                '-output-directory=' + temp_dir,
                tex_file_path
            ]
            process = subprocess.run(pdflatex_command, capture_output=True, text=True)

            if not os.path.exists(pdf_file_path):
                # If PDF fails, return the error log
                log_content = process.stderr
                if os.path.exists(log_file_path):
                    with open(log_file_path, 'r', encoding='utf-8') as f:
                        log_content = f.read()
                return JsonResponse({'success': False, 'log': log_content})

            # 5. If PDF is successful, execute pandoc for DOCX
            pandoc_command = ['pandoc', tex_file_path, '-o', docx_file_path]
            subprocess.run(pandoc_command, capture_output=True, text=True)

            # 6. Read and encode the generated files
            result = {'success': True}

            with open(pdf_file_path, 'rb') as f:
                pdf_bytes = f.read()
                result['pdf'] = base64.b64encode(pdf_bytes).decode('utf-8')

            if os.path.exists(docx_file_path):
                with open(docx_file_path, 'rb') as f:
                    docx_bytes = f.read()
                    result['docx'] = base64.b64encode(docx_bytes).decode('utf-8')

            return JsonResponse(result)

    except Exception as e:
        return JsonResponse({'success': False, 'log': f'An unexpected server error occurred: {str(e)}'}, status=500)
