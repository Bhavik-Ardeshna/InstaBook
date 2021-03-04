from django import forms
from comment.models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(required=True)

    class Meta:
        model = Comment
        fields = ('comment',)
