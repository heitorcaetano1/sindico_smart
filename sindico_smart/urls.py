from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from sindico_smart import settings

urlpatterns = [
    path('agendamentos/', include('apps.agendamentos.urls')),
    path('apartamentos/', include('apps.apartamentos.urls')),
    path('moradores/', include('apps.inquilino.urls')),
    path('proprietarios/', include('apps.proprietario.urls')),
    path('financeiro/', include('apps.financeiro.urls')),
    path('', include('apps.core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('condominio/', include('apps.condominios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
