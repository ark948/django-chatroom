from django.db import models
from markdownx.models import MarkdownxField



# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()
    author = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title