# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u'Hello World')

def django(request):
    return HttpResponse(u'Hello Django')
