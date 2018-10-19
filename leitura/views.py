from django.shortcuts import render

from estacoes.models import Estacao
from leitura.models import Leitura


def list_leituras(request):
    estacao = Estacao.objects.all()
    leituras = Leitura.objects.all()
    return render(request, 'leituras/lista_leituras.html', {
        'leituras': leituras, 'estacao': estacao})
