from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# blog/forms.py
from .models import Comment
from .models import Post, Tag
# blog/forms.py
from .widgets import TagWidget

class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=TagWidget(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        tags_data = self.cleaned_data['tags']
        # Split the tags by comma and strip whitespace
        tags = [tag.strip() for tag in tags_data.split(',') if tag.strip()]
        return tags

    def save(self, commit=True):
        post = super().save(commit)
        # Create or get tags and associate them with the post
        for tag_name in self.cleaned_data['tags']:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return post


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