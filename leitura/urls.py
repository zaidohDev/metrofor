from django.urls import path
from .views import list_leituras
urlpatterns = [
    path('leituras/', list_leituras, name='list_leituras'),
]