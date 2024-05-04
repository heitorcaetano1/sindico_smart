from django.db import models
from django.core.validators import RegexValidator


class Proprietario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome Proprietário')
    identidade = models.CharField(max_length=100, help_text='Numero da Indentidade')
    orgao = models.CharField(max_length=100, help_text='Orgão emissor')
    nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=100, help_text='Nacionalidade')
    proficao = models.CharField(max_length=100, help_text='Profissão')
    ddd_validator = RegexValidator(regex=r'^\d{2}$', message="O DDD deve conter 2 dígitos.")
    ddd = models.CharField(validators=[ddd_validator], max_length=2, help_text='Digite o DDD')
    telefone_validator = RegexValidator(regex=r'^\d{8,9}$', message="O número de telefone deve conter 8 ou 9 dígitos.")
    tel_cont1 = models.CharField(validators=[telefone_validator], max_length=9, help_text='Digite o número de telefone')
    contato2 = models.CharField(validators=[telefone_validator], max_length=9, help_text='Digite o número de telefone')
    email = models.EmailField(help_text='E-mail de contato')
    bloco = models.IntegerField()
    apartamento = models.IntegerField()

    def __str__(self):
        return self.nome
