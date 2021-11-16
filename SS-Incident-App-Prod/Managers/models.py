from django.db import models

# Create your models here.

class ManagerModel(models.Model):
    name = models.CharField(max_length=80, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    
    class Meta():
        
        ordering = ['name']
        
    
    def __str__(self):
        return self.name