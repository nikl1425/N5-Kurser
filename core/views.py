from django.shortcuts import render
from django.http import HttpResponse
from django.views import View



# Create your views here

class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

class CourseView(View):
    def get(self, request):
        return render(request, "courses.html")




    

