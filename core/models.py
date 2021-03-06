from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created = models.DateTimeField('Criado em', auto_now_add=True)
    updated = models.DateField('Atualizado em:', auto_now=True)
    
    class Meta:
        abstract = True    

class Cliente(Base):
    criador_cliente = models.ForeignKey(User, related_name='Criador_Cliente', verbose_name='Criador_Cliente', on_delete=models.CASCADE)
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
    def __str__(self):
        return self.nome

class Servico(Base):
    servico = models.CharField('Serviço', max_length=100,)
    descricao = models.TextField('Descrção', max_length=40)
    criador_servico = models.ForeignKey(User, related_name='Criador_Servico', verbose_name='Criador_Servico', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.servico
            
class Os(Base):
    criador_os = models.ForeignKey(User, related_name='Criador_Os', verbose_name='Criador_Os', on_delete=models.CASCADE)
    cliente = models.ForeignKey('core.Cliente', verbose_name='Cliente', on_delete=models.CASCADE, default=' ')
    relato = models.TextField('Relato', max_length=200)
    defeito_encontrado = models.TextField('Defeito', max_length=200)
    servico = models.ForeignKey('core.Servico', verbose_name='Serviço', on_delete=models.DO_NOTHING)
    desc_serv = models.TextField('Descrição do Serviço', max_length=200)
    garantia = models.DateField('Garantia')
    serv_valor = models.DecimalField('Valor do Serviço', decimal_places=2, max_digits=8)
    pec_valor = models.DecimalField('Valor das Peças', decimal_places=2, max_digits=8, null=True)

    
    @property
    def total(self):
        '''Calcula o valor total da Ordem de Serviço on time'''
        return self.serv_valor + self.pec_valor
