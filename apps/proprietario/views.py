from django.shortcuts import render, get_object_or_404
from .models import Proprietario


def lista_proprietario(request):
    proprietario = Proprietario.objects.all()
    return render(request, 'templates/proprietarios.html',
                  {'proprietario': proprietario})


def detalhes_proprietario(request, nome_propietario):
    proprietario = get_object_or_404(Proprietario,
                                     nome__icontains=nome_propietario)
    return render(request,
                  'templates/proprietario.html',
                  {'proprietario': proprietario})
