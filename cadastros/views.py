from .models import Cidade, Estado

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


class EstadoCreate(CreateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index-2')


class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index-2')
