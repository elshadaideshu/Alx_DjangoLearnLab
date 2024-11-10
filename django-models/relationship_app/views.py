# relationship_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is Admin
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

# Check if user is Librarian
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

# Check if user is Member
def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    """View for Admin users."""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """View for Librarian users."""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    """View for Member users."""
    return render(request, 'relationship_app/member_view.html')