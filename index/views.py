from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "Basic/index.html")


def sslverify(request):
    return HttpResponse(open("58AF068D2EDF53CC7C4DE9F66C653E04.txt").read())