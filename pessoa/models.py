from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256, verbose_name="Nome Completo")
    data_nascimento = models.DateField(null=True, verbose_name="Data Nascimento")
    ativo = models.BooleanField(default=True, verbose_name="Ativo")
