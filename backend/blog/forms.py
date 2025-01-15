from django import forms
from markdownx.fields import MarkdownxFormField



class AddPostForm(forms.Form):
    title = forms.CharField(required=True, max_length=200)
    body = MarkdownxFormField()
    