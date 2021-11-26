from django.urls import path
from .views import EstadoCreate, EstadoUpdate

urlpatterns = [
    # Criar todos os endereços/rotas
    # path('endereço/', MinhaView.as_view(), name='referência/apelido'),

    path('inserir/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    
]
