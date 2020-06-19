from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

from .models import Renta_devolucion


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def devolver(request,id_renta):
    L:Renta_devolucion = Renta_devolucion.objects.get(id=id_renta)
    L.fecha_de_Devuelta = timezone.now()
    L.estado = True
    L.vehiculo.estado = True
    L.vehiculo.save()
    L.save()
    return redirect('/App1/renta_devolucion/')