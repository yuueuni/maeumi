from django.http.response import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import RegisterForm


# Create your views here.
def home(request):
    return render(request, 'bigday/home.html')


def test(request):
    return render(request, 'bigday/testView.html')


def report(request):
    return render(request, 'bigday/finalReport.html')


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'bigday/test.html', {'new_user':new_user})
        else:
            user_form = RegisterForm()

        return render(request, 'bigday/test.html', {'form':user_form})