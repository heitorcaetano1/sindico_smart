from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.inquilino.models import Inquilinos
import barcode
from barcode.writer import ImageWriter
from io import BytesIO


class Conta(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    tipo = models.CharField(max_length=10,
                            choices=(('pagar', 'Pagar'), ('receber', 'Perceber')))
    status = models.CharField(max_length=10,
                              choices=(('pendente',  'Pendente'), ('pago', 'Pago')))


class FluxoCaixa(models.Model):
    data_movimento = models.DateField()
    tipo = models.CharField(max_length=10,
                            choices=(('entrada', 'Entrada'), ('saida', 'Saída')))
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    conta = models.ForeignKey(Conta, on_delete=models.SET_NULL, null=True)


class Auditoria(models.Model):
    acao = models.CharField(max_length=64)
    descricao = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Conta)
def auditoria_save(sender, instance, **Kwargs):
    Auditoria.objects.create(acao='delete', descricao=f'Conta{instance.descricao} salva ou atualizada.')

def auditoria_delete(sender, instance, **Kwargs):
    Auditoria.objects.create(acao='delete', descricao=f'Conta{instance.descricao} exxxcluída.')

class Boleto(models.Model):
    inquilino = models.ForeignKey(Inquilinos, on_delete=models.PROTECT, related_name='boletos')
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimanto = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    status_pagamento = models.CharField(max_length=20, choices=(('pendente', 'Pendente'), ('pago', 'Pago')))
    arquivo_pdf = models.FileField(upload_to='boletos/', null=True, blank=True)
    codigo_barras = models.ImageField(upload_to='codigo_barras/', blank=True)

    def gerar_codigo_barras(self):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.numero_identificacao}', writer=ImageWriter())
        buffer = BytesIO()
        ean.writer(buffer)
        self.codigo_barras.save(f'codigo de barras_{self.id}.png', save=False)
        return self.codigo_barras

    def __str__(self):
        return f'{self.descricao} - {self.inquilino}'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detalhes_boleto', kwargs={'pk': self.pk})
