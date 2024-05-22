from django.shortcuts import render
from .models import Funcionarios


def detalhe_funcionario(request, user_id):
    funcionario = Funcionarios.objects.get(user__id=user_id)
    context = {'funcionario': funcionario}
    return render(request, 'base.html', context)
