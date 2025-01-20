from django.db import models

# Create your models here.
class TaskManagement(models.Model):
    Title = models.CharField(max_length=100) #checks the range of data which can be written by user
    Description = models.TextField() #the description can be long so it dont have to be set
    Status = models.BooleanField(default = False) #when we first create todo list the list is incomplete as work is pending
    Created_at = models.DateTimeField(auto_now_add=True) #shows the time of creation
    