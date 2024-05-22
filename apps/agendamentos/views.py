from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Agendamentos
from .forms import AgendamentoForm


def agendamentos(request):
    template = loader.get_template('agendamentos.html')
    return HttpResponse(template.render())


def lista_agenda(request):
    agendamento = Agendamentos.objects.all()
    context = {'agendamento': agendamento}
    template = loader.get_template('agendamentos.html')
    return HttpResponse(template.render(context, request))


def criar_agendamento(request):
    template = loader.get_template('agendar.html')
    form = AgendamentoForm()
    context = {'form': form}

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamentos.html')
    else:
        form = AgendamentoForm()
    return HttpResponse(template.render(context, request))
