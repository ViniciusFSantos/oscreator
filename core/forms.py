from dataclasses import fields
from django import forms
from .models import Cliente, Servico, Os

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        context_object_name = 'servico_form'
        fields = ('servico', 'descricao')

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        context_object_name = 'cliente_form'
        fields = ('nome', 'cpf_cnpj', 'rg_ie', 'telefone1', 'telefone2', 'email', 'endereco', 'bairro', 'cidade', 'uf')

class OsForm(forms.ModelForm):
    class Meta:
        model = Os
        context_object_name = 'os_form'
        fields = ('cliente', 'relato', 'defeito_encontrado', 'servico', 'desc_serv', 'garantia', 'serv_valor', 'pec_valor')
        
    
