from rest_framework import viewsets, filters
from .models import Categoria, Produto, Pedido, ItemPedido
from .serializers import (
    CategoriaSerializer, ProdutoSerializer,
    PedidoSerializer, ItemPedidoSerializer
)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.select_related('categoria').all()
    serializer_class = ProdutoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao']

    def get_queryset(self):
        qs = super().get_queryset()
        for key, val in self.request.query_params.items():
            if key.startswith('meta_'):
                campo = key[5:]
                qs = qs.filter(**{f'metadados__{campo}': val})
        return qs


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.prefetch_related('itens__produto').all()
    serializer_class = PedidoSerializer


class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.select_related('pedido', 'produto').all()
    serializer_class = ItemPedidoSerializer