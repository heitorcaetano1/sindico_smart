from django import forms
from .models import Agendamentos


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamentos
        fields = ['hora', 'dia', 'periodo', 'categoria',
                  'inquilino', 'bloco', 'apartamento']
