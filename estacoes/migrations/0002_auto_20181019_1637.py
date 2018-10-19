# Generated by Django 2.1.1 on 2018-10-19 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gates', '0001_initial'),
        ('estacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacao',
            name='gates',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gates.Gate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estacao',
            name='nome',
            field=models.TextField(choices=[('CHI', '1 - Chico da Silva'), ('JAL', '2 - José de Alencar'), ('SBE', '3 - São Benedito'), ('BEN', '4 - Benfica'), ('PCI', '5 - Padre Cícero'), ('POR', '6 - Porangabussu'), ('COU', '7 - Couto Fernandes'), ('JUK', '8 - Juscelino Kubsheck'), ('PAR', '9 - Parangaba'), ('VIP', '10 - Vila Pery'), ('SAT', '11 - Manoel Sátiro'), ('MON', '12 - Mondubim'), ('ESP', '13 - Esperança'), ('ARA', '14 - Aracapé'), ('ALT', '15 - Alto Alegre'), ('RAQ', '16 - Raquel de Queiróz'), ('VIT', '17 - Virgílio Távora'), ('MAR', '18 - Maracanaú'), ('JER', '19 - Jereissati'), ('CAB', '20 - Carlito Benevides')]),
        ),
    ]
