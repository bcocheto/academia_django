from django.contrib import admin

from .models import Cliente, Funcionario, Ficha

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nascimento', 'sexo')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nascimento', 'sexo')

@admin.register(Ficha)
class FichaAdmin(admin.ModelAdmin):
    list_display = ('exercicios','tipo_treino','objetivo')