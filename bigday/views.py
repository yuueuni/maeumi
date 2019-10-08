from django.http.response import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'bigday/index.html')
