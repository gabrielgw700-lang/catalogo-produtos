from rest_framework import serializers
from .models import Categoria, Produto, Pedido, ItemPedido


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class ItemPedidoSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = ItemPedido
        fields = ['id', 'produto', 'quantidade', 'preco_unitario', 'subtotal']


class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True, read_only=True)
    total = serializers.ReadOnlyField()

    class Meta:
        model = Pedido
        fields = ['id', 'status', 'criado_em', 'atualizado_em', 'itens', 'total']