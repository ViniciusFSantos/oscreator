from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from core.models import Servico
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = 'index.html'
    pass    

class MainBoard(ListView):
    model = Servico
    template_name = 'mainboard'
    context_object_name = 'servicos'
    
    
    '''def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.not_auth)'''