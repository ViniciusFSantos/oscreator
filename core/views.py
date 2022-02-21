from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import auth

class IndexView(TemplateView):
    template_name = 'index.html'
    pass    


class MainBoard(TemplateView):
    template_name = 'mainboard.html'
    #!!TODO
    usuario = auth.get_user()
    pass