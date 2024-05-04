from django.db import models
from apps.condominios.models import Condominios


class Bloco(models.Model):
    numero = models.IntegerField()
    condominio = models.ManyToManyField(Condominios)

    def __str__(self):
        return self.numero
