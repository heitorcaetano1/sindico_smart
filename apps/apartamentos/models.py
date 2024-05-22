from django.db import models
from apps.bloco.models import Bloco
from apps.proprietario.models import Proprietario
from apps.inquilino.models import Inquilinos


class Apartamentos(models.Model):
    numero = models.IntegerField()
    bloco = models.OneToOneField(Bloco, on_delete=models.PROTECT)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.PROTECT)
    morador = models.ForeignKey(Inquilinos, on_delete=models.PROTECT)

    def __str__(self):
        return self.numero, self.bloco
