from django.db import models

# Create your models here.
class student(models.Model):
    firstname = models.CharField(max_length = 100)
    secondname = models.CharField(max_length = 100)
    email = models.EmailField()
    regno = models.CharField(max_length = 100)
    age = models.IntegerField()


    def __str__(request):
       return (self.firstname)
