from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel

# Create your views here.
def home(request):
    x=Hotel.objects.all()
    return render(request,"dey.html",{"x":x})


