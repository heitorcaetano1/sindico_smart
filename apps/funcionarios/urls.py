from django.urls import path
from .views import detalhe_funcionario, FuncionariosList

urlpatterns = [
    path('funcionario/<int:user_id>/', detalhe_funcionario, name='usuario'),
    path('funcionarios', FuncionariosList.as_view(), name='funcionario_list')
]
