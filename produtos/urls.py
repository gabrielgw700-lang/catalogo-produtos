from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, CategoriaViewSet, PedidoViewSet, ItemPedidoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'itens-pedido', ItemPedidoViewSet) 

urlpatterns = router.urls
