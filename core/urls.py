from django.contrib import admin
from django.urls import path
from .views import IndexView, MainBoard
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('mainboard/',MainBoard.as_view(), name='mainboard'),
]