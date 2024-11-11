# relationship_app/admin_view.py
from django.shortcuts import render

def admin_view(request):
    return render(request, 'relationship_app/admin.html')  # Ensure this template exists