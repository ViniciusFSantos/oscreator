from urllib import request
from django.shortcuts import render
from django.views.generic import TemplateView, View

class IndexView(TemplateView):
    template_name = 'index.html'
    pass    


class MainBoard(View):
    template_name = 'mainboard.html'
    not_auth = 'notauth.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.not_auth)