from django.urls import path, include
from .views import detalhe_funcionario

urlpatterns = [
    path('funcionario/<int:user_id>/', detalhe_funcionario, name='usuario')
]
