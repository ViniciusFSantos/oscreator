from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Cliente, Servico, Os

class ServicoForm(forms.ModelForm):
    model = Servico
    fields = ('servico', 'descricao')

class ClienteForm(forms.ModelForm):
    model = Cliente
    fields = ('nome', 'cpf_cnpj', 'rg_ie', 'telefone1', 'telefone2', 'email', 'endereco', 'bairro', 'cidade', 'uf')
