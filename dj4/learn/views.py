# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm

def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()

    return render(request, 'index.html', {'form': form})

def home(request):
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})

def add(request):
    a = request.GET.get('a', None)
    b = request.GET.get('b', None)
    a = int(a)
    b = int(b)
    return HttpResponse(str(a + b))
