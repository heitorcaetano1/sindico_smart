from django.urls import path
from .views import AgendamentoView, CriarAgendamentoView, ListaAgendaView


urlpatterns = [
    path('agenda', ListaAgendaView.as_view(), name='agendamentos/lista'),
    path('agendar/', CriarAgendamentoView.as_view(), name='agendar/criar')
]
