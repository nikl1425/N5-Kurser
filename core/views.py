from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Course, CourseCategory


# Helper Functions








# Create your views here

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

class CourseView(View):
    def get(self, request):
        courses = Course.objects.order_by("-Created")
        course_categories = CourseCategory.objects.all()

        context = {
            "courses": courses,
            "categories": course_categories
        }

        return render(request, "courses.html", context=context)




    

