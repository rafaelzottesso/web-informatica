from .models import Cidade, Estado

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy


class EstadoCreate(CreateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')


class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')


class EstadoList(ListView):
    model = Estado
    template_name = 'cadastros/listas/estados.html'


#######################################


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'habitantes', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'habitantes', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')


class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidades.html'

#######################################
