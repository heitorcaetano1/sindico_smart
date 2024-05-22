from django.urls import path
from . import views

urlpatterns = [
    path('relatorio/csv', views.gerar_relatorio_csv, name='gerar_relatorio_csv'),
    path('relatorio/pdf', views.gerar_relatorio_pdf, name='gerar_relatorio_pdf'),
    path('criar_boleto/', views.criar_boleto, name='criar_boleto'),
    path('enviar-boleto/<int:boleto_id>/', views.enviar_boleto, name='enviar_boleto'),
    path('financeiro/', views.financeiro, name='financeiro'),
]
