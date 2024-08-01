from django.urls import path
from .views import InquilinoListView, detalhe_morador, InquilinosCreateView, excluir_inquilio

urlpatterns = [
    path('inquilinos/', InquilinoListView.as_view(), name='inquilino-list'),
    path('moradores/inquilinos/<int:id_inquilino>/', detalhe_morador, name='detalhe_morador'),
    path('inquilinos/cadastrar/', InquilinosCreateView.as_view(), name='inquilino-criar'),
    path('inquilinos/<int:pk>/excluir', excluir_inquilio, name='excluir_inquilino'),
]
