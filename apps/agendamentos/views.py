from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import AgendamentoForm
from .models import Agendamentos


class AgendamentoView(TemplateView):
    template_name = 'agendamentos.html'


class ListaAgendaView(TemplateView):
    template_name = 'agendamentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agendamento'] = Agendamentos.objects.all()
        return context


from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import AgendamentoForm  # the location of your forms file


class CriarAgendamentoView(FormView):
    template_name = 'agendar.html'
    form_class = AgendamentoForm
    success_url = reverse_lazy('agendamentos/lista')

    def form_valid(self, form):
        agendamento = form.save(commit=False)

        # add any other processing (validation, setting additional attributes etc.) here

        agendamento.save()
        return super().form_valid(form)
