from django.db import models

# Create your models here.
class Post(models.Model):
    title = model.CharField(max_length=50)
    content = model.CharField(max_length=100)
    
    def __str__(self):
        return self.title