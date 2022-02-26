from django.views import generic
from core.models import Servico, Cliente, Os
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.TemplateView):
    template_name = 'index.html'
    pass    

class MainBoard(LoginRequiredMixin, generic.TemplateView):
    template_name = 'mainboard.html'
    pass

class ClienteView(LoginRequiredMixin, generic.ListView):
    template_name = 'cliente.html'
    context_object_name = 'clientes'
    def get_queryset(self):
        return Cliente.objects.all()

class ServicoView(LoginRequiredMixin, generic.ListView):
    template_name = 'servico.html'
    context_object_name = 'servicos'
    def get_queryset(self):
        return Servico.objects.all()

class OsView(LoginRequiredMixin, generic.ListView):
    template_name = 'os.html'
    context_object_name = 'OSs'
    def get_queryset(self):
        return Os.objects.all()