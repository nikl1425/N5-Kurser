from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.
class Course(models.Model):
    Name = models.CharField(max_length=80)
    Description = models.TextField(max_length=2000)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField()

class Lesson(models.Model):
    Name = models.CharField(max_length=80)
    Order = models.IntegerField(validators=[MaxLengthValidator(20), MinLengthValidator(0)])
    VideoLink = models.URLField()
    
class LessonContent(models.Model):
    Content = models.TextField(max_length=2000)
