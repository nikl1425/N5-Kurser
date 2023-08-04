from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
import datetime

class CourseCategory(models.Model):
    Name = models.CharField(max_length=80, primary_key=True)
    Description = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return self.Name

class ProgrammingLanguage(models.Model):
    Name = models.CharField(max_length=80)
    Description = models.TextField(max_length=2000)


# Create your models here.
class Course(models.Model):
    LANG = [
        ("DK", "Dansk"),
        ("EN", "engelsk")
    ]

    Name = models.CharField(max_length=80)
    Description = models.TextField(max_length=2000)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField()
    Created = models.DateField(default=datetime.date.today)
    Category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, null=True)
    Lang = models.CharField(choices=LANG, max_length=2, default="DK")
    ProgrammingLang = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.Name


class Lesson(models.Model):
    Name = models.CharField(max_length=80)
    Order = models.IntegerField(validators=[MaxLengthValidator(20), MinLengthValidator(0)])
    VideoLink = models.URLField()
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.Name

    
class LessonContent(models.Model):
    BlockName = models.CharField(default="block", max_length=80)
    DisplayOrder = models.IntegerField(default=0, validators=[MaxLengthValidator(20), MinLengthValidator(0)])
    CONTENT_TYPE = [
        ("C", "code"),
        ("T", "text"),
    ]
    TypeOfContent = models.CharField(choices=CONTENT_TYPE, max_length=1, default="T")
    Content = models.TextField(max_length=2000)
    Lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.BlockName
