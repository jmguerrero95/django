from .models import Book
from .models import Author
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'
class AutorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'