from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView

from core.models import Cliente, Os, Servico

from .forms import ClienteForm, OsForm, ServicoForm


# ----- Views -----
class IndexView(TemplateView):
    template_name = 'index.html'
    pass    

class MainBoard(LoginRequiredMixin, TemplateView):
    template_name = 'mainboard.html'


class ClienteView(LoginRequiredMixin, ListView):
    template_name = 'cliente.html'
    context_object_name = 'clientes'
    def get_queryset(self):
        return Cliente.objects.filter(criador_cliente = self.request.user.id)

class ServicoView(LoginRequiredMixin, ListView):
    template_name = 'servico.html'
    context_object_name = 'servicos'
    def get_queryset(self):
        return Servico.objects.filter(criador_servico = self.request.user.id)

class OsView(LoginRequiredMixin, ListView):
    template_name = 'os.html'
    context_object_name = 'OSs'
    def get_queryset(self):
        return Os.objects.filter(criador_os = self.request.user.id)

class ClienteOsSpecifcView(DetailView):
    template_name ='clienteos.html'
    context_object_name ='cliente'
    model = Cliente

class ServicoOsSpecifcView(DetailView):
    template_name ='servicoos.html'
    context_object_name ='servico'
    model = Servico

    
# ---------------------
# ------- Create ------
class ClienteFormView(LoginRequiredMixin, FormView):
    template_name = 'novocliente.html'
    form_class = ClienteForm
    def form_valid(self, form):
        form.save()        
        return HttpResponseRedirect('/mainboard/clientes')

class ServicoFormView(LoginRequiredMixin, FormView):
    template_name = 'novoservico.html'
    form_class = ServicoForm
    def form_valid(self, form):
        form.save()        
        return HttpResponseRedirect('/mainboard/servicos')

class OsFormView(FormView):
    template_name = 'novaos.html'
    form_class = OsForm
    def form_valid(self, form):
        form.save()        
        return HttpResponseRedirect('/mainboard/os')

# ---------------------
# ------- Update ------
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'clienteupdate.html'
    fields = [
        'nome',
        'cpf_cnpj',
        'rg_ie',
        'telefone1',
        'telefone2',
        'email',
        'endereco',
        'bairro',
        'cidade',
        'uf',
    ]
    success_url = '/mainboard/clientes'

class ServicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Servico
    template_name = 'servicoupdate.html'
    fields = [
        'servico', 
        'descricao',
    ]
    success_url = '/mainboard/servicos'

# ---------------------
# ------ Delete ------
