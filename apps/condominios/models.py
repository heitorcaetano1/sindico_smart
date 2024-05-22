from django.db import models


class Condominios(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do condomínio')
    logo = models.ImageField(upload_to='logo_Condominio/', null=True, blank=True)

    def __str__(self):
        return self.nome
