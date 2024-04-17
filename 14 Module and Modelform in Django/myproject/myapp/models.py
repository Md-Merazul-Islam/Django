from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name= models.TextField(default='Rohim')
    address = models.TextField()
    
    def  __str__(self):
        return f' Roll : {  self.roll}  Name : {self.name}'
    