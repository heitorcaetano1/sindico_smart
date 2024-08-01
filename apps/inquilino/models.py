from django.db import models
from django.core.validators import RegexValidator
from apps.bloco.models import Bloco
from apps.condominios.models import Condominios
from apps.proprietario.models import Proprietario


class Inquilinos(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Inquilino')
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
    bloco = models.ForeignKey(Bloco, on_delete=models.PROTECT)
    apartamento = models.IntegerField()
    condominio = models.ForeignKey(Condominios, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.nome


class Dependentes(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Dependente')
    parentesco = models.CharField(max_length=100, help_text='Parentesco')
    identidade = models.CharField(max_length=100, help_text='Numero da Indentidade')
    orgao = models.CharField(max_length=100, help_text='Orgão emissor')
    nascimento = models.DateField()
    ddd_validator = RegexValidator(regex=r'^\d{2}$', message="O DDD deve conter 2 dígitos.")
    ddd = models.CharField(validators=[ddd_validator], max_length=2, help_text='Digite o DDD')
    telefone_validator = RegexValidator(regex=r'^\d{8,9}$', message="O número de telefone deve conter 8 ou 9 dígitos.")
    tel_cont1 = models.CharField(validators=[telefone_validator], max_length=9, help_text='Digite o número de telefone')
    contato2 = models.CharField(validators=[telefone_validator], max_length=9, help_text='Digite o número de telefone')
    email = models.EmailField(help_text='E-mail de contato')
    inquilino = models.ForeignKey(Inquilinos, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Veiculos(models.Model):
    placa = models.CharField(max_length=100, help_text='Placa do veículo')
    marca = models.CharField(max_length=100, help_text='marca do veículo')
    modelo = models.CharField(max_length=100, help_text='modelo do veículo')
    cor = models.CharField(max_length=100, help_text='cor do veículo')
    dono = models.ManyToManyField(Inquilinos)

    def __str__(self):
        return self.placa


class Animais(models.Model):
    especie = models.CharField(max_length=100, help_text='Especie')
    quantidade = models.IntegerField()
    vacinacao = models.CharField(max_length=100, help_text='Vacinado')
    dono = models.ManyToManyField(Inquilinos)

    def __str__(self):
        return self.especie
