from rest_framework import serializers, viewsets, routers
from .models import Book
from .serializer import BookSerializer


class BookApiView(viewsets.ModelViewSet):
    queryset = Book.objects.filter(published=True)
    serializer_class = BookSerializer


router = routers.DefaultRouter()
router.register(r'book/list', BookApiView)
