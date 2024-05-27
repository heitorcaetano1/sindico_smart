from django.urls import path
from .views import InquilinoListView, InquilinoDetailView, DetalhesMoredorView

urlpatterns = [
    path('inquilinos/', InquilinoListView.as_view(), name='inquilino-list'),
    path('inquilinos/<int:pk>/', InquilinoDetailView.as_view(), name='inquilino-detail'),
    path('inquilinos/detalhes/<str:nome_inquilino>/', DetalhesMoredorView.as_view(), name='detalhes-morador'),
]
