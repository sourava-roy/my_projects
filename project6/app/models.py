from django.db import models

# Create your models here.
class StudentData(models.Model):
    sname = models.CharField(max_length=100)
    spno = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username
