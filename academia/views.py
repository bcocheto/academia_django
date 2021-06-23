from abc import ABC

from chartjs.views.lines import BaseLineChartView
from django.db.models import Count
from django.views.generic import TemplateView, ListView

from academia.models import Cliente, Funcionario, Ficha, Pessoa


class IndexView(TemplateView):
    template_name = "index.html"


class ClientView(TemplateView):
    template_name = "client.html"

    def get_context_data(self, **kwargs):
        context = super(ClientView, self).get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.order_by('nome').all()
        return context


class FuncView(TemplateView):
    template_name = "func.html"

    def get_context_data(self, **kwargs):
        context = super(FuncView, self).get_context_data(**kwargs)
        context['funcionario'] = Funcionario.objects.order_by('nome').all()
        return context


class FichaView(ListView):
    template_name = "ficha.html"
    model = Cliente

    def get_context_data(self, **kwargs):
        context = super(FichaView, self).get_context_data(**kwargs)
        id = self.kwargs['id']
        context['ficha'] = Ficha.objects.filter(cliente_id=id).first
        return context

    def get_queryset(self):
        id = self.kwargs['id']
        return Ficha.objects.filter(id=id)


class DadosAcademiaView(BaseLineChartView):

    def get_labels(self):
        labels = []
        queryset = Cliente.objects.all()
        for cliente in queryset:
            labels.append(cliente.sexo)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Cliente.objects.annotate(total=Count('sexo'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado
