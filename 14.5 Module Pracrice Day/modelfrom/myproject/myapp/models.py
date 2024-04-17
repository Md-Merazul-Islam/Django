from django.db import models

# Create your models here.

# class Student(models.Model):
#     name = models.CharField(max_length=20)
#     roll = models.IntegerField(primary_key=True)
#     address = models.TextField()
#     big_auto_field = models.BigAutoField(primary_key=True)
#     old_primary_key = models.AutoField(primary_key=True)

#     # New BigAutoField
#     new_primary_key = models.BigAutoField(primary_key=True)

#     # Other fields in your model
#     other_field = models.CharField(max_length=100)
#     def __str__(self):
#         return f'Roll : {self.roll}  - {self.name}'
    
    
    
#     from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email_field = models.EmailField()
    roll = models.IntegerField(primary_key=True)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    boolean_field = models.BooleanField()
    date_time= models.DateTimeField()
    duration_field = models.DurationField()
    file_field = models.FileField(upload_to='files/')

    message = models.TextField()
    