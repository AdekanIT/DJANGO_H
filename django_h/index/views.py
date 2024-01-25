from django.shortcuts import render


# Create your views here.


def regist_form(request):
    return render(request, 'regist.html')


def states(request):
    return render(request, 'states.html')


def home(request):
    return render(request, 'home.html')