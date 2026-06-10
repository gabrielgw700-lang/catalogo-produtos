from django.contrib import admin
from .models import Categoria, Produto, Pedido, ItemPedido


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'preco', 'categoria']
    list_filter = ['categoria']
    search_fields = ['nome']


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'criado_em']
    inlines = [ItemPedidoInline]
    list_filter = ['status']


@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pedido', 'produto', 'quantidade', 'preco_unitario']