# compiler\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('compile/', views.compile_latex, name='compile_latex'),
]