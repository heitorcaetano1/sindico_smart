from django import forms
from .models import Agendamentos


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamentos
        fields = ['hora', 'dia', 'periodo', 'categoria',
                  'inquilino', 'bloco', 'apartamento']

    def clean(self, *args, **kwargs):
        cleaned_data = super(AgendamentoForm, self).clean(*args, **kwargs)
        return cleaned_data