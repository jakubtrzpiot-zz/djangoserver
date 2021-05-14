from django.db import models

class Account(models.Model):
    full_name = models.CharField(max_length=50)
    nick = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    creation_date = models.DateTimeField('creation date')
    
