from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.methos == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)