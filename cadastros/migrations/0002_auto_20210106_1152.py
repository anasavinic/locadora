# Generated by Django 3.1.2 on 2021-01-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='fim',
            field=models.DateField(verbose_name='Data de Devolução'),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='inicio',
            field=models.DateField(verbose_name='Data de Locação'),
        ),
    ]
