from django.http import HttpResponse
from django.template import loader
from .models import Inquilinos, Animais, Veiculos, Dependentes


def detalhes_morador(request, nome_inquilino):
    inquilinos = Inquilinos.objects.filter(nome__icontains=nome_inquilino)

    detalhes_moradores = []
    for inquilino in inquilinos:
        dependente = Dependentes.objects.filter(inquilino=inquilino)
        animais = Animais.objects.filter(inquilino=inquilino)
        veiculos = Veiculos.objects.filter(onquilino=inquilino)
        detalhes_moradores.append({
            'inquilino': inquilino,
            'dependente': dependente,
            'animais': animais,
            'veiculos': veiculos
        })
    template = loader.get_template('morador.html')
    context = {'detalhes_moradores': detalhes_moradores}
    return HttpResponse(template.render(context, request))


def lista_morador(request):
    moradores = Inquilinos.objects.all().values()
    template = loader.get_template('moradores.html')
    context = {'moradores': moradores}
    return HttpResponse(template.render(context, request))
