from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'bigday/home.html')


def testView(request):
    return render(request, 'bigday/testView.html')

