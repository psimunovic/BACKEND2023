from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def appejemplo(request):
    return HttpResponse("Esta es una APP en DJANGO!")

def appejemplo2(request):
  template = loader.get_template('pag1.html')
  return HttpResponse(template.render())