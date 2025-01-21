from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth import get_user_model



# Create your models here.

class TimeStampModel(models.Model):
    """Abstract base class that adds created_at and updated_at fields to models."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # this model is abstract, do not create table for it




class Post(TimeStampModel):
    title = models.CharField('Title', max_length=200)
    body = CKEditor5Field('Body', config_name='extends')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')

    def __str__(self) -> str:
        return f"<Post Blog object {self.title}>"