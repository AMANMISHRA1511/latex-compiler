# latex-compiler
# Codexa - Modern LaTeX Compiler

![Codexa Logo](https://i.ibb.co/68v8zPn/codexa-logo.png)

A professional, responsive web application to compile LaTeX code into high-quality PDF and DOCX documents in real-time. Codexa provides a modern, dark-themed IDE-like experience right in your browser.

![Screenshot of Codexa in action](https://via.placeholder.com/800x450.png/010409/C9D1D9?text=Codexa+Live+Editor+and+Output+View)
*(A screenshot or GIF of the application would go here)*

## ✨ Features

-   **Live LaTeX Editing**: Write your code with professional syntax highlighting using CodeMirror.
-   **Real-time PDF Compilation**: Instantly compile your LaTeX code and view the resulting PDF.
-   **DOCX Export**: Seamlessly export your document to Microsoft Word (.docx) format using Pandoc.
-   **Fully Responsive Design**: Works beautifully on desktop, tablet, and mobile devices.
-   **Professional UI**: A clean, modern dark theme designed for a distraction-free experience.
-   **Resizable Panes**: On desktop, drag the divider to resize the editor and output panes to your preference.
-   **Detailed Error Logging**: Get clear, actionable feedback if your LaTeX code has any errors.

## 🛠 Tech Stack

-   **Backend**: Django, Python
-   **Frontend**: HTML5, CSS3 (Tailwind CSS), JavaScript (CodeMirror)
-   **System Dependencies**: TeX Live (pdflatex), Pandoc

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

1.  **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
    -   **Important**: During installation, make sure to check the box that says **"Add Python to PATH"**.

2.  **A LaTeX Distribution**: This provides the `pdflatex` compiler.
    -   **Windows**: [Install MiKTeX](https://miktex.org/download)
    -   **macOS**: `brew install --cask mactex`
    -   **Linux (Ubuntu/Debian)**: `sudo apt-get install -y texlive-full`

3.  **Pandoc**: This is used for converting to DOCX.
    -   [Install Pandoc](https://pandoc.org/installing.html)
    -   **Important**: Ensure that the command-line tools for both LaTeX and Pandoc are added to your system's PATH during installation.

## 🚀 Installation and Setup

Follow these steps to get a copy of the project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/django-latex-compiler.git
cd django-latex-compiler
