# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    title ='Home Page'
    context={
        'title':title,
    }
    return render(request, 'index.html',context)

def about(request):
    title='About Us'
    context ={
        'title':title
    }
    return render(request, 'about.htlm',context)