from django.views import generic
from core.models import Servico
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.TemplateView):
    template_name = 'index.html'
    pass    

class MainBoard(LoginRequiredMixin, generic.ListView):
    template_name = 'mainboard.html'
    context_object_name = 'servicos'
    def get_queryset(self):
        return Servico.objects.all()
    
