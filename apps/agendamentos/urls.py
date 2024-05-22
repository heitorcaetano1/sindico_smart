from django.urls import path
from .views import lista_agenda, criar_agendamento


urlpatterns = [
    path('agendamentos/', lista_agenda, name='agendamentos'),
    path('agendar/', criar_agendamento, name='agendar')
]
