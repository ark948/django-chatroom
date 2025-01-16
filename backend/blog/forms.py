from django import forms
from ckeditor.widgets import CKEditorWidget
from django_ckeditor_5.widgets import CKEditor5Widget



from blog.models import Post
    



class NewPostForm(forms.ModelForm):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["body"].required = False

      class Meta:
          model = Post
          fields = ("title", "body")
          widgets = {
              "body": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }