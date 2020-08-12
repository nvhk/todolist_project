from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDosy(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    memo = models.TextField(blank=True)
    wykonanie = models.DateTimeField(null=True, blank=True)
    wazne = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

    def __str__(self):
        return self.title
        
    