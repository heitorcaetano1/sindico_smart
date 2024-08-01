from django.contrib import admin
from .models import Apartamentos


class ApartamentosAdmin(admin.ModelAdmin):
    list_display = ('numero', 'bloco')


admin.site.register(Apartamentos, ApartamentosAdmin)
