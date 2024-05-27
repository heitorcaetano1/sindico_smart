from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import AgendamentoForm, Agendamentos


class AgendamentoView(View):
    template_name = 'agendamentos.html'

    def get(self, request):
        return render(request, self.template_name)


class ListaAgendaView(View):
    template_name = 'agendamentos.html'

    def get(self, request):
        agendamento = Agendamentos.objects.all()
        context = {'agendamento': agendamento}
        return render(request, self.template_name, context)


class CriarAgendamentoView(View):
    template_name = 'agendar.html'

    def get(self, request):
        form = AgendamentoForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamentos/lista')
        else:
            return render(request, self.template_name, {'form': form})
