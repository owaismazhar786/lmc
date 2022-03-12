from django.db import models
from sqlalchemy import null
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=50, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name
