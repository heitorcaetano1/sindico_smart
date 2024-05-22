from django.urls import path
from .views import detalhe_apartamento, lista_apartamento


urlpatterns = [
    path('apartamento/<int:id>', detalhe_apartamento, name='detalhe_apartamento'),
    path('apartamentos', lista_apartamento, name='lista_apartamento')
]
