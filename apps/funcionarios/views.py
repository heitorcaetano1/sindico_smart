from django.shortcuts import render
from django.views.generic import ListView

from .models import Funcionarios


def detalhe_funcionario(request, user_id):
    funcionario = Funcionarios.objects.get(user__id=user_id)
    context = {'funcionario': funcionario}
    return render(request, 'base.html', context)


class FuncionariosList(ListView):
    model = Funcionarios


def profile_view(request):
    user_profile = Funcionarios.objects.get(user=request.user)
    return render(request, 'profile.htm', {'user_profile': user_profile})
