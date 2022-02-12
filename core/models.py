from ast import Delete
from django.db import models
from tkinter import CASCADE

class Base(models.Model):
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateField('Atualizado em:', auto_now=True)
    
    class Meta:
        abstract = True    

class Cliente(Base):
    nome = models.CharField('Nome', max_length=120)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=14)
    rg_ie = models.CharField('RG/IE', max_length=12)
    telefone1 =models.CharField('Telefone1', blank=True, null=True, max_length=11)
    telefone2 = models.CharField('Telefone2', blank=True, null=True, max_length=11)
    email = models.EmailField('E-mail', max_length=50, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=120)
    bairro = models.CharField('Bairro', max_length=100)
    cidade = models.CharField('Cidade', max_length=50)
    uf = models.CharField('UF', max_length=2)

class Servico(Base):
    servico = models.CharField('Serviço', max_length=100,)
    descricao = models.TextField('Descrção', max_length=40)
    
class Os(Base):
    cliente = models.ForeignKey('core.Cliente', verbose_name='Cliente', on_delete=models.CASCADE)
    relato = models.TextField('Relato', max_length=200)
    defeito_encontrado = models.TextField('Defeito', max_length=200)
    servico = models.ForeignKey('core.Servico', verbose_name='Serviço', on_delete=models.DO_NOTHING)
    desc_serv = models.TextField('Descrição do Serviço', max_length=200)
    garantia = models.DateField('Garantia')
    serv_valor = models.DecimalField('Valor do Serviço', decimal_places=2, max_digits=8)
    pec_valor = models.DecimalField('Valor das Peças', decimal_places=2, max_digits=8, null=True)
    #!! TODO Total serv_valor + pec_valor 
        