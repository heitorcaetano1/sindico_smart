from django.contrib import admin
from .models import Condominios


class CondominioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logo')


admin.site.register(Condominios, CondominioAdmin)
