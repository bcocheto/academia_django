import uuid

from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Pessoa(models.Model):
    OPCOES = (
        ('Masculino', _('Masculino')),
        ('Feminino', _('Feminino')),
        ('Não Definido', _('Não Definido')),
    )
    nome = models.CharField("Nome", max_length=255)
    nascimento = models.DateField("Data Nascimento", help_text="Formato DD/MM/AAAA")
    email = forms.EmailInput()
    foto = StdImageField('Foto', null=True, blank=True, upload_to=get_file_path,
                         variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    sexo = models.CharField("Sexo", max_length=12, choices=OPCOES)

    class Meta:
        abstract = True
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['id']

    def __str__(self):
        return self.nome


class Cliente(Pessoa):
    matricula = models.IntegerField("Matrícula", default=1, unique=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Exercicio(models.Model):
    repeticoes = models.IntegerField("Repetições")
    nome = models.CharField("Nome", max_length=200)
    tipo = models.CharField("Tipo de Treino", max_length=200)
    descricao = models.TextField("Descrição", max_length=500)


class Funcionario(Pessoa):
    matricula = models.IntegerField("Matrícula", default=1, unique=True)
    descricao = models.TextField("Descrição", max_length=500, blank=True)

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"


class Ficha(models.Model):
    nome = models.CharField("Nome da Ficha", max_length=100, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    exercicios = models.ManyToManyField(Exercicio)

    class Meta:
        verbose_name = "Ficha"
        verbose_name_plural = "Fichas"
