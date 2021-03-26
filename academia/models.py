from django.db import models


class Cliente(models.Model):
    nome = models.CharField("Nome", max_length=255)
    nascimento = models.DateField("Data Nascimento")
    sexo = models.CharField("Sexo", max_length=1)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Funcionario(models.Model):
    nome = models.CharField("Nome", max_length=255)
    nascimento = models.DateField("Data de Nascimento")
    sexo = models.CharField("Sexo", max_length=1)


class Ficha(models.Model):
    nome_cliente = models.CharField("Nome", max_length=255)
    nome_instrutor = models.CharField("Nome do Instrutor", max_length=255)
    exercicios = models.CharField("Exercicios", max_length=400)
    tipo_treino = models.CharField("Tipo de Treino", max_length=64)
