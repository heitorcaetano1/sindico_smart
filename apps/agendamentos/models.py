from django.db import models

from apps.condominios.models import Condominios
from apps.inquilino.models import Inquilinos


class Agendamentos(models.Model):
    objetos_choices = [('Ch', 'Churrasqueira'),
                       ('SF', 'Salão de Festas'),
                       ('SJ', 'Salão de Jogos'),
                       ('Md', 'Mudança')]
    hora = models.CharField(max_length=100, help_text='Horário')
    dia = models.DateField()
    periodo = models.CharField(max_length=100, help_text='Manhã, Tarde ou Noite')
    categoria = models.CharField(max_length=100, choices=objetos_choices)
    inquilino = models.ForeignKey(Inquilinos, on_delete=models.SET_NULL, null=True)
    bloco = models.IntegerField()
    apartamento = models.IntegerField()
    condominio = models.ForeignKey(Condominios, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.categoria
