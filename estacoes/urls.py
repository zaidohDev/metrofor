from django.urls import path
from .views import list_estacoes, show_estacoes

urlpatterns = [
    path('list/', list_estacoes, name='list_estacoes'),
    path('show/<int:id>/', show_estacoes, name='show_estacoes'),
]