from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage' : 'Replacing the variable in the template engine'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'myname' : 'Med Larbi'}
    return render(request, 'rango/about.html', context=context_dict)