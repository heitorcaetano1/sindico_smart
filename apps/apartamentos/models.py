from django.db import models
from apps.bloco.models import Bloco
from apps.proprietario.models import Proprietario
from apps.inquilino.models import Inquilinos
from apps.condominios.models import Condominios


class Apartamentos(models.Model):
    numero = models.IntegerField()
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT, null=True, blank=True)
    morador = models.ForeignKey(Inquilinos, on_delete=models.PROTECT, null=True, blank=True)
    condominio = models.ForeignKey(Condominios, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.numero}, {self.bloco}'
