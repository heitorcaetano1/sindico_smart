from django import forms
from .models import Conta, FluxoCaixa, Boleto


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['descricao', 'valor', 'data_vencimento', 'tipo', 'status']


class FluxiCaixaForm(forms.ModelForm):
    class Meta:
        model = FluxoCaixa
        fields = ['data_movimento', 'tipo', 'valor', 'conta']


class BoletoForm(forms.ModelForm):
    class Meta:
        model = Boleto
        fields = ['descricao', 'valor', 'data_vencimanto']
