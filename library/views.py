"""
Renders the landing page of the application.
"""

from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')
