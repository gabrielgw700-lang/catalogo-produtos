from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = router.urls
