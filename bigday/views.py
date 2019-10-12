from django.http.response import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'bigday/home.html')


def test(request):
    return render(request, 'bigday/testView.html')


def report(request):
    return render(request, 'bigday/finalReport.html')