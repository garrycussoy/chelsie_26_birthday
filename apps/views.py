# Import django related tools
from django.shortcuts import render

"""
Following is a function to show main page
"""
def index(request):
  # Render main page
  return render(request, 'index.html')
