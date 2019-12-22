from rest_framework import routers

from .viewsets import BookViewSet
from .viewsets import AutorViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('author', AutorViewSet)

urlpatterns = router.urls