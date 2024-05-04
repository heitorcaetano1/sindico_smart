from django.contrib import admin
from .models import Dependentes, Inquilinos, Animais, Veiculos

admin.site.register(Dependentes)

admin.site.register(Inquilinos)

admin.site.register(Animais)

admin.site.register(Veiculos)
