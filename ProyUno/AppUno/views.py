from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
  datos = {'clase': 'Programación III', 'Profesor': 'Luis Amaya'}
  return render(request, 'uno.html', datos)


def Hola(request):
    return HttpResponse('Bienvenidos a Hola!')
