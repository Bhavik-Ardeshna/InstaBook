from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('body',)
