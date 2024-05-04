from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamentos
from apps.condominios.models import Condominios


class Funcionarios(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome funcionário')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.ManyToManyField(Departamentos)
    condominio = models.ForeignKey(Condominios, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
