from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# blog/forms.py
from .models import Comment
from .models import Post, Tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()  # Queryset for available tags

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = "Your Comment"

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user