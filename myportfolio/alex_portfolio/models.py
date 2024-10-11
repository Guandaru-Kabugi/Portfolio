from django.db import models

# Create your models here.


class Message(models.Model):
    email = models.EmailField(max_length=155, unique=False,null=False)
    name = models.CharField(max_length=100,null=False)
    subject = models.CharField(max_length=100,null=False)
    message = models.TextField(max_length=300,null=False)