from django.db import models
from django import forms


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=255)
    nascimento = models.DateField("Data Nascimento")
    sexo = models.CharField("Sexo", max_length=1)
    foto = forms.FileField()

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Funcionario(models.Model):
    nome = models.CharField("Nome", max_length=255)
    nascimento = models.DateField("Data de Nascimento")
    sexo = models.CharField("Sexo", max_length=1)
    is_instrutor = models.BooleanField(default=1)
    foto = forms.FileField()


class Ficha(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    instrutor = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=True, blank=True)
    exercicios = models.CharField("Exercicios", max_length=255)
    tipo_treino = models.CharField("Tipo de Treino", max_length=64)
    objetivo = models.CharField("Objetivo do Cliente", max_length=200, null=True, blank=True)
