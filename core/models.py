from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.conf import settings
import datetime

LANG = [
    ("DK", "Danish"),
    ("EN", "Enlish")
]

LEVEL = [
    (1, "Beginner"),
    (2, "Intermediate"),
    (3, "Advanced")
]

MAX_SMALL_DEFAULT = 80
MAX_LONG_DEFAULT = 2000


class CourseCategory(models.Model):
    Name = models.CharField(max_length=MAX_SMALL_DEFAULT, primary_key=True)
    Description = models.TextField(max_length=MAX_LONG_DEFAULT)

    def __str__(self) -> str:
        return self.Name

class ProgrammingLanguage(models.Model):
    Name = models.CharField(max_length=80)
    Description = models.TextField(max_length=2000)

    def __str__(self) -> str:
        return self.Name


# Create your models here.
class Course(models.Model):
    Name = models.CharField(max_length=MAX_SMALL_DEFAULT)
    Description = models.TextField(max_length=MAX_LONG_DEFAULT)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    Created = models.DateField(default=datetime.date.today)
    Category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, null=True)
    Lang = models.CharField(choices=LANG, max_length=2, default="DK")
    ProgrammingLang = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, null=True)
    level = models.IntegerField(choices=LEVEL, default=1)
    published = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.Name
    
    # def save(self, *args, **kwargs):
    #     try:
    #         this = Course.objects.get(id=self.id)
    #         if this.Image:
    #             this.Image.delete()
    #     except:
    #         pass
    #     super(Course, self).save(*args, **kwargs)


class Lesson(models.Model):
    Name = models.CharField(max_length=MAX_SMALL_DEFAULT)
    Order = models.IntegerField(validators=[MaxLengthValidator(20), MinLengthValidator(0)])
    VideoLink = models.URLField()
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.Name

    
class LessonContent(models.Model):
    BlockName = models.CharField(default="block", max_length=MAX_SMALL_DEFAULT)
    DisplayOrder = models.IntegerField(default=0, validators=[MaxLengthValidator(20), MinLengthValidator(0)])
    CONTENT_TYPE = [
        ("C", "code"),
        ("T", "text"),
    ]
    TypeOfContent = models.CharField(choices=CONTENT_TYPE, max_length=1, default="T")
    Content = models.TextField(max_length=MAX_LONG_DEFAULT)
    Lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.BlockName
