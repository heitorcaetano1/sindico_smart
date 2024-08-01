from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamentos
from apps.condominios.models import Condominios


class Funcionarios(models.Model):

    nome = models.CharField(max_length=100, help_text='Nome funcionário')
    cargo = models.ManyToManyField(Departamentos, related_name="funcionarios_cargo", blank=True)
    condominio = models.ForeignKey(Condominios, on_delete=models.CASCADE, null=True)
    foto_usuario = models.ImageField(upload_to='fotos_usuario/', null=True, blank=True)
    user = models.OneToOneField(User, related_name='Nome_usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
