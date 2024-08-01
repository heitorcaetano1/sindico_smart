from django.urls import path
from .views import detalhes_proprietario, lista_proprietario, registro_proprietario


urlpatterns = [
    path('proprietario', detalhes_proprietario, name='proprietario'),
    path('proprietarios/', lista_proprietario, name='proprietarios'),
    path('registro_proprietario', registro_proprietario, name='registro_proprietario'),
    path('detalhes/<int:proprietario_id>/', detalhes_proprietario, name='detalhes_proprietario'),
]
