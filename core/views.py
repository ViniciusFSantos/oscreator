from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView
from core.models import Servico

class IndexView(TemplateView):
    template_name = 'index.html'
    pass    

class MainBoard(View):
    template_name = 'mainboard.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.not_auth)