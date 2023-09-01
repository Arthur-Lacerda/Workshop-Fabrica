from rest_framework import routers
from .views import LivroViewSet,LojaViewSet

router = routers.DefaultRouter()
router.register(r'Loja', LojaViewSet)
router.register(r'Livro', LivroViewSet)
urlpatterns = router.urls