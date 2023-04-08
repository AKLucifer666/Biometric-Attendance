from django.db import models

# Create your models here.

class studentsData(models.Model):
    name = models.CharField(max_length=125)
    rollno = models.CharField(max_length=125)
    contact = models.CharField(max_length=125)
    branch = models.CharField(max_length=125)
    password = models.TextField()
    photo_coordinates = models.TextField()

class attendance(models.Model):
    name = models.CharField(max_length=125)
    rollno = models.CharField(max_length=125)
    branch = models.CharField(max_length=125)
    date = models.CharField(max_length=125)
