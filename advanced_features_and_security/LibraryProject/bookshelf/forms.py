# LibraryProject/bookshelf/forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book  # Specify the model to use
        fields = ['title', 'author', 'published_date']  # Include the fields you want in the form
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})  # Use a date input widget
        }

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)