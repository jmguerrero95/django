from rest_framework import viewsets
from .models import Book
from .models import Author
from .serializer import BookSerializer
from .serializer import AutorSerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class AutorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AutorSerializer