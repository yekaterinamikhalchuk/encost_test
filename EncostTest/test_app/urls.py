from .views import DurationsList
from django.urls import path

urlpatterns = [
    path('', DurationsList.as_view()),
]