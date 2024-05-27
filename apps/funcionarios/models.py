from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.departamentos.models import Departamentos
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from apps.condominios.models import Condominios


class Funcionarios(AbstractUser):
    nome = models.CharField(max_length=100, help_text='Nome funcionário')
    cargo = models.ManyToManyField(Departamentos, related_name="funcionarios_cargo")
    condominio = models.ForeignKey(Condominios, on_delete=models.PROTECT, null=True, blank=True)
    foto_usuario = models.ImageField(upload_to='fotos_usuario/', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name="funcionarios_groups")
    user_permissions = models.ManyToManyField(Permission, related_name="funcionarios_user_permissions")

    def is_administracao_or_contabilidade(self):
        return self.cargo.filter(nome__in=['Adminstração', 'Contabilidade']).exists()

    def __str__(self):
        return self.nome
