from django import forms
from post.models import Post

from django.forms import ClearableFileInput


class NewPostForm(forms.ModelForm):
    content = forms.FileField()
    caption = forms.CharField()
    tags = forms.CharField()

    class Meta:
        model = Post
        fields = ('content', 'caption', 'tags')
