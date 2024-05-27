from .views import CondominioCreate, CondominioEdit
from django.urls import path


urlpatterns = [
    path('novo', CondominioCreate.as_view(), name='criar_condominio'),
    path('editar/<int:pk>/',
         CondominioEdit.as_view(), name='editar_condominio'),
]
