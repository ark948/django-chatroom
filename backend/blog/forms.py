from django import forms
from markdownx.fields import MarkdownxFormField
from django_summernote.widgets import SummernoteWidget
from ckeditor.widgets import CKEditorWidget



from blog.models import PostV2, PostV3



class AddPostForm(forms.Form):
    title = forms.CharField(required=True, max_length=200)
    body = MarkdownxFormField()




class AddPostFormV2(forms.ModelForm):
    class Meta:
        model = PostV2
        fields = ["title", "body"]

    body = forms.CharField(widget=SummernoteWidget)



# this uses ckeditor 4 which DID NOT WORK
class AddPostFormV3(forms.ModelForm):
    class Meta:
        model = PostV3
        fields = ['title', 'body']

    body = forms.CharField(widget=CKEditorWidget())
    
    


from blog import models
from django_ckeditor_5.widgets import CKEditor5Widget
class AddPostFormV4(forms.ModelForm):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

      class Meta:
          model = models.PostV4
          fields = ("title", "body")
          widgets = {
              "body": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }