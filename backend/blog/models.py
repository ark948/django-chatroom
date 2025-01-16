from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



# Create your models here.




class Post(models.Model):
    title = models.CharField('Title', max_length=200)
    body = CKEditor5Field('Body', config_name='extends')
    author = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)