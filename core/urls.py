from django.contrib import admin
from django.urls import path
from .views import IndexView, MainBoard, ClienteView, ServicoView, OsView, ClienteFormView, ServicoFormView, OsFormView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('mainboard/', MainBoard.as_view(), name='mainboard'),
    path('mainboard/clientes', ClienteView.as_view(), name='clientes'),
    path('mainboard/servicos', ServicoView.as_view(), name='servicos'),
    path('mainboard/os', OsView.as_view(), name='os'),
    path('mainboard/clientes/new', ClienteFormView.as_view(), name='clientes_new'),
    path('mainboard/servicos/new', ServicoFormView.as_view(), name='servicos_new'),
    path('mainboard/os/new', OsFormView.as_view(), name='os_new'),
]