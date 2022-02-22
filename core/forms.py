from dataclasses import fields
from django import forms
from .models import Cliente, Servico, Os

class ServicoForm(forms.ModelForm):
    model = Servico
    fields = ('servico', 'descricao')
