from .models import Cidade, Estado

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from django.urls import reverse_lazy


class EstadoCreate(CreateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Estados'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context 


class EstadoUpdate(UpdateView):
    model = Estado
    fields = ['sigla', 'nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-estado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Estado'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context


class EstadoList(ListView):
    model = Estado
    template_name = 'cadastros/listas/estados.html'


#######################################


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'habitantes', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Cidades'
        context['botao'] = 'Cadastrar'
        context['cor'] = 'primary'
        return context


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['nome', 'habitantes', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cidade'
        context['botao'] = 'Salvar'
        context['cor'] = 'success'
        return context


class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/listas/cidades.html'

#######################################
