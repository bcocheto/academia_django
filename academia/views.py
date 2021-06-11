from django.views.generic import TemplateView, ListView

from academia.models import Cliente, Funcionario, Exercicio, Ficha


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
        context['ficha'] = Ficha.objects.filter(id=id).first
        return context

    def get_queryset(self):
        id = self.kwargs['ficha_id']
        return Cliente.objects.filter(id=id)
