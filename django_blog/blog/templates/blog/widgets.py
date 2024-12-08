# blog/widgets.py

from django import forms

class TagWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({'placeholder': 'Add tags separated by commas', 'class': 'tag-input'})