from django.shortcuts import render

from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')