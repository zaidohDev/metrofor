from django.shortcuts import render, get_object_or_404
from estacoes.models import Estacao
from leitura.models import Leitura


def list_estacoes(request):
    estacoes = Estacao.objects.all()
    return render(request, 'estacoes/lista_estacoes.html', {'estacoes': estacoes})


def show_estacoes(request, id):
    leituras = Leitura.objects.order_by('gate')
    estacoes = get_object_or_404(Estacao, pk=id)
    return render(request, 'estacoes/show_estacoes.html', {'estacoes': estacoes, 'leituras': leituras})


