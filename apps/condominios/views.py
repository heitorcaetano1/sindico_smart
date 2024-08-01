from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Condominios
from apps.funcionarios.models import Funcionarios


class CondominioCreate(CreateView):
    model = Condominios
    fields = ['nome', 'logo']

    def form_valid(self, form):
        obj = form.save(commit=False)
        try:
            funcionario = Funcionarios.objects.get(user=self.request.user)
            obj.id_condominio = funcionario.condominio
            funcionario.save()
            messages.success(self.request, f'Condominio {obj.nome} Criado com Sucesso!')
            return redirect(reverse('home'))

        except Funcionarios.DoesNotExist:
            messages.error(self.request, 'Nenhuma entrada correspondente de '
                                         'Funcionários encontrada para este usuário')

        return super().form_valid(form)


class CondominioEdit(UpdateView):
    model = Condominios
    fields = ['nome', 'logo']
    success_url = reverse_lazy('home')


def condominios_info(request):

    condominio = None
    if request.user.is_authenticated:
        try:
            condominio = Condominios.objects.get(user=request.user.funcionario.condominio)
        except Condominios.DoesNotExist:
            condominio = None
    else:
        condominio = None

    return {'condominio': condominio}

def base_template(request):
    if request.user.is_authenticated:  # ensure user is logged in
        employee = request.user.employee  # get employee object related to user
        try:
            condominio = Condominios.objects.get(
                nome=employee.condominio)  # get condominium related to logged in employee
        except Condominios.DoesNotExist:
            condominio = None  # handle the case where the employee's condominium does not exist

        return render(request, 'base.html', {'condominio': condominio})  # pass the condominium to the base template
    else:
        return render(request, 'base.html', {})
