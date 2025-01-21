from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.author.id, filename)




class StudentFile(models.Model):
    title = models.CharField('Title', max_length=50, null=False)
    file = models.FileField('File', upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='files')