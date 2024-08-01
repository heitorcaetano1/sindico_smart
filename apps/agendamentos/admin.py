from django.contrib import admin
from .models import Agendamentos


class AgendamentosAdmin(admin.ModelAdmin):
    list_display = ('dia', 'periodo', 'categoria')


admin.site.register(Agendamentos, AgendamentosAdmin)
