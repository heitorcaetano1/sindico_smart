from django.shortcuts import render, get_object_or_404
from .models import Apartamentos


def detalhe_apartamento(request, id):
    apartamento = get_object_or_404(Apartamentos, pk=id)
    return render(request, 'apartamento.html',
                  {'apartamento': apartamento})


def lista_apartamento(request):
    apartamentos = Apartamentos.objects.all()
    return render(request, 'teplates/apartamentos.html',
                  {'apartartamentos': apartamentos})
