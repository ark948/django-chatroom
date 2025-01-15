from django.db import models
from markdownx.models import MarkdownxField
from ckeditor.fields import RichTextField



# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()
    author = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



class PostV2(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)




class PostV3(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    author = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)




from django_ckeditor_5.fields import CKEditor5Field
class PostV4(models.Model):
    title = models.CharField('Title', max_length=200)
    body = CKEditor5Field('Body', config_name='extends')
    author = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)