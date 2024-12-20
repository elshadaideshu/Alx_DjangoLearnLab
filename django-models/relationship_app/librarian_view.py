# relationship_app/views/librarian_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is Librarian
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')