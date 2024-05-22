from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('agendamentos/', include('apps.agendamentos.urls')),
    path('apartamentos/', include('apps.apartamentos.urls')),
    path('moradores/', include('apps.inquilino.urls')),
    path('proprietarios/', include('apps.proprietario.urls')),
    path('financeiro/', include('apps.financeiro.urls')),
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
