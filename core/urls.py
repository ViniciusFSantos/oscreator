from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    path('mainboard/', views.MainBoard.as_view(), name='mainboard'),
    path('mainboard/clientes', views.ClienteView.as_view(), name='clientes'),
    path('mainboard/servicos', views.ServicoView.as_view(), name='servicos'),
    path('mainboard/os', views.OsView.as_view(), name='os'),
    path('mainboard/clientes/new', views.ClienteFormView.as_view(), name='clientes_new'),
    path('mainboard/servicos/new', views.ServicoFormView.as_view(), name='servicos_new'),
    path('mainboard/os/new', views.OsFormView.as_view(), name='os_new'),
    path('mainboard/clientes/<pk>', views.ClienteUpdateView.as_view(), name='clientes_update'),
    path('mainboard/servicos/<pk>', views.ServicoUpdateView.as_view(), name='servicos_update'),
    path('mainboard/clienteos/<pk>', views.ClienteOsSpecifcView.as_view(), name='cliente_os'),
]
