from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(".well-known/pki-validation/58AF068D2EDF53CC7C4DE9F66C653E04.txt", views.sslverify)
]