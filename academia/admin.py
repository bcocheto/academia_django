from django.contrib import admin

from .models import Cliente, Funcionario, Ficha, Exercicio


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'matricula', 'nascimento', 'sexo')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'matricula', 'nascimento', 'sexo')


@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cliente', 'funcionario')


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'repeticoes')
