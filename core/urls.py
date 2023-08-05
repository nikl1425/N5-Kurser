from django.urls import path
from core.views import CourseView, IndexView

urlpatterns = [
    path("", IndexView.as_view()),
    path("courses", CourseView.as_view())
]