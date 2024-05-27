from django import forms
from .models import Dependentes, Veiculos, Animais


class DependentesForm(forms.ModelForm):
    class Meta:
        model = Dependentes
        fields = '__all__'


class VeiculosForm(forms.ModelForm):
    class Meta:
        model = Veiculos
        fields = '__all__'


class AnimaisForm(forms.ModelForm):
    class Meta:
        model = Animais
        fields = '__all__'
