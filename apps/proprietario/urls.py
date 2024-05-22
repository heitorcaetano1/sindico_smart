from django.urls import path
from .views import detalhes_proprietario, lista_proprietario


urlpatterns = [
    path('proprietario', detalhes_proprietario, name='proprietario'),
    path('proprietarios', lista_proprietario, name='proprietarios')
]
