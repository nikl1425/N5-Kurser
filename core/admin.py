from django.contrib import admin
from .models import Course, Lesson, LessonContent
# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonContent)