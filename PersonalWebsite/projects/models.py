from django.db import models

# Create your models here.
class Project(models.Model):
    category_options = [('WebApplication', 'Web Application'),('MoblieApplication', 'Moblie Application'),('SciencePaper', 'Science Paper')]
    title = models.CharField(max_length=32)
    description = models.TextField()
    tools = models.CharField(max_length=255, default="Not specified")
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    status = models.BooleanField(default=False)
    category = models.CharField(max_length=256,choices=category_options)
    image = models.ImageField(upload_to="images/")
    
    

