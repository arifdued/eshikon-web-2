from django.db import models

# Create your models here.
class user_info(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + '' + self.lname
    
from django.utils.timezone import now

class post(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)
    username = models.CharField(max_length=100, default='defult username')


    def __str__(self):
        return f'{self.author} - {self.timestamp}'
    