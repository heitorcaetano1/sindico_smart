from unittest import loader
from 
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Inquilinos, Animais, Veiculos, Dependentes


class InquilinoListView(ListView):
    model = Inquilinos
    template_name = 'inquilinos_list.html'
    context_object_name = 'inquilinos'


class InquilinoDetailView(DetailView):
    model = Inquilinos
    template_name = 'inquilino_detail.html'
    context_object_name = 'inquilino'


class DetalhesMoredorView(View):
    template_name = 'morador.html'

    def get(self, request, nome_inquilino):
        inquilinos = Inquilinos.objects.filter(nome_icontains=nome_inquilino)
        detalhes_moradores = []

        for inquilino in inquilinos:
            dependente = Dependentes.objects.filter(inquilino=inquilino)
            animais = Animais.objects.filter(inquilino=inquilino)
            veiculos = Veiculos.objects.filter(inquilino=inquilino)
            detalhes_moradores.append({
                'inquilino': inquilino,
                'dependente': dependente,
                'animais': animais,
                'veiculos': veiculos,
            })

            context = {'detalhes_moradores': detalhes_moradores}
            return HttpResponse(loader.render_to_string(self.template_name, context, request))


class InquilinoCreateView(CreateView):
    model = Inquilinos
    form_class = InquilinoForm
    template_name =
