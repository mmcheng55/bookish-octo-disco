from django.urls import path
from . import views


app_name = "encr"
urlpatterns = [
    path("", views.index, name="index"),    
]
