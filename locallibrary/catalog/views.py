from django.shortcuts import render
from django.http import HttpResponse

def empty_view(request):
    return HttpResponse('This is empty now.')
