from django.contrib import admin
from .models import Funcionarios


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo_nome', 'foto_usuario')

    def cargo_nome(self, obj):
        return obj.cargo.nome
    cargo_nome.short_description = 'Cargo'


admin.site.register(Funcionarios, FuncionarioAdmin)
