from django.urls import path

from . import views

appname = "qrcode"
urlpatterns = [
    path("", views.index, name="index"),
]