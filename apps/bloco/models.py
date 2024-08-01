from django.db import models
from apps.condominios.models import Condominios


class Bloco(models.Model):
    numero = models.CharField(max_length=10)
    condominio = models.ManyToManyField(Condominios, blank=True)

    def __str__(self):
        return self.numero
