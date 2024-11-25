# LibraryProject/bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Your Name")
    email = forms.EmailField(required=True, label="Your Email")

    # You can add more fields as needed