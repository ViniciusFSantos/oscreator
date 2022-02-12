from django.contrib import admin
from core.models import Cliente, Servico, Os

@admin.register(Cliente)
class Cliente(admin.ModelAdmin):
    list_display = ('nome', 'cpf_cnpj', 'rg_ie', 'telefone1', 'telefone2', 'email', 'endereco', 'bairro',
    'cidade', 'uf')

@admin.register(Servico)
class Servico(admin.ModelAdmin):
    list_display = ('servico', 'descricao')

@admin.register(Os)
class Os(admin.ModelAdmin):
    list_display = ('cliente', 'relato', 'defeito_encontrado', 'servico', 'desc_serv', 'garantia', 'serv_valor', 'pec_valor')

