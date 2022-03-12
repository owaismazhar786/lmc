from distutils.command.upload import upload
from django.db import models

# Create your models here.


class blogpost(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.title
