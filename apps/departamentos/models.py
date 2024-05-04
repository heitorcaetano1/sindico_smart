from django.db import models
from apps.condominios.models import Condominios


class Departamentos(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do departamento')
    condominio = models.ManyToManyField(Condominios)

    class Meta:
        app_label = 'departamentos'


    def __str__(self):
        return self.nome
