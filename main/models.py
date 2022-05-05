from django.db import models
from django.forms import CharField
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    video = EmbedVideoField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=50, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=50, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name
