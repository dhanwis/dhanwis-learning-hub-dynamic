from django.db import models

# Create your models here.
class Course(models.Model):
    image= models.ImageField(upload_to='admin/courses', null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    duraction = models.CharField(max_length=200, null=True, blank=True)

class Company(models.Model):
    image = models.ImageField(upload_to='admin/companies', null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)

class Placement(models.Model):
    image = models.ImageField(upload_to='admin/palcements', null=True, blank=True)
    company_name = models.CharField(max_length=500, null=True, blank=True)
    designation = models.CharField(max_length=500, null=True, blank=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to='admin/gallery', null=True, blank=True)
    shorts_url = models.CharField(max_length=500, null=True, blank=True)
    yt_url = models.CharField(max_length=500, null=True, blank=True)
