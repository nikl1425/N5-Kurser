from django.contrib import admin
from .models import Course, Lesson, LessonContent, CourseCategory
# Register your models here.
admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonContent)