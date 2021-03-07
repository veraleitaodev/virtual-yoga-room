from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = ['body', 'name']
