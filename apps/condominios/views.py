from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
from .models import Condominios
from django.contrib.auth.models import User



class CondominioCreate(CreateView):
    model = Condominios
    fields = ['nome', 'logo']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Condominio Criado com Sucesso!')


class CondominioEdit(UpdateView):
    model = Condominios
    fields = ['nome', 'logo']
