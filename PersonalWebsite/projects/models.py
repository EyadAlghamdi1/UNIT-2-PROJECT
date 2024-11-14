from django.db import models

# Create your models here.
class Project(models.Model):
    category_options = [('WebApplication', 'Web Application'),('MoblieApplication', 'Moblie Application'),('SciencePaper', 'Science Paper')]
    title = models.CharField(max_length=32)
    description = models.TextField()
    status = models.BooleanField()
    category = models.CharField(max_length=256,choices=category_options)
    image = models.ImageField(upload_to="images/")
    
    

