from django.db import models


class Agendamentos(models.Model):
    objetos_choices = [('Ch', 'Churrasqueira'), ('SF', 'Salão de Festas'), ('SJ', 'Salão de Jogos')]
    hora = models.CharField(max_length=100, help_text='Horario')
    dia = models.DateField()
    periodo = models.CharField(max_length=100, help_text='Manhã, Tarde ou Noite')
    tipo = models.CharField(max_length=100, choices=objetos_choices)

    def __str__(self):
        return self.tipo
