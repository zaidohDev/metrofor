from django.db import models
from estacoes.models import Estacao, ESTACOES_CHOICES

GATES_CHOICES = (
    ('BLQ-01', 'E-001'),
    ('BLQ-02', 'E-002'),
    ('BLQ-03', 'E-003'),
    ('BLQ-04', 'E-004'),
    ('BLQ-05', 'E-005'),
    ('BLQ-06', 'E-006'),
    ('BLQ-07', 'E-007'),
    ('BLQ-08', 'E-008'),
    ('BLQ-09', 'E-009'),
    ('BLQ-11', 'E-011'),
    ('BLQ-12', 'E-012'),
    ('BLQ-01', 'M-001'),
    ('BLQ-02', 'M-002'),
    ('BLQ-03', 'M-003'),
    ('BLQ-04', 'M-004'),
    ('BLQ-05', 'M-005'),
    ('BLQ-06', 'M-006'),
    ('BLQ-07', 'M-007'),
    ('BLQ-08', 'M-008'),
    ('BLQ-09', 'M-019'),
    ('BLQ-10', 'M-010'),
    ('BLQ-11', 'M-011'),
    ('BLQ-12', 'E-012'),
)

TIPO_CHOICES = (
    ('1', 'Eletrônico'),
    ('2', 'Mecânico'),
    )


class Leitura(models.Model):
    gate = models.TextField(choices=GATES_CHOICES)
    tipo = models.TextField(choices=TIPO_CHOICES)
    nome = models.TextField(max_length=255, choices=ESTACOES_CHOICES)
    ler_entrada = models.IntegerField(default=0000000)
    ler_saida = models.IntegerField(default=0000000)
    estacao_leitura = models.ManyToManyField(Estacao)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "Entrada: {0} - Saída: {1} - Gate: {2} - Estação: {3} - Data/Hora: {4}".format(
            self.ler_entrada, self.ler_saida, self.gate, self.estacao_leitura, self.created_at)

