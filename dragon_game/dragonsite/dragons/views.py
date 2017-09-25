# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("You <u>must</u> create a <b>dragon</b>! <img src=dragon.jpg>")