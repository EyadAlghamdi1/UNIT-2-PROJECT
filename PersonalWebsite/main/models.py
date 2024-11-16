from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    category_options = [('Front End', 'Front End'),('Back End', 'Back End'),('Tool', 'Tool')]
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=256,choices=category_options)
    

