from django.urls import path
from .views import detalhes_morador, lista_morador


urlpatterns = [
    path('morador/busca/<str:nome_inquilino>/',
         detalhes_morador, name='detalhes_morador'),
    path('moradores/', lista_morador, name='lista_inquilinos'),
]
