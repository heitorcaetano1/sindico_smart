from django.db import models


class Condominios(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do condomínio')

    def __str__(self):
        return self.nome
