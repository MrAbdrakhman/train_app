# api/views.py

from rest_framework import generics
from .models import Category, Quote, Word, Idiom
from .serializers import CategorySerializer, QuoteSerializer, WordSerializer, IdiomSerializer

class QuoteRandomView(generics.ListAPIView):
    queryset = Quote.objects.order_by('?')[:1]
    serializer_class = QuoteSerializer

class QuoteListCreateView(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class WordListCreateView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class WordRetrieveView(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

class IdiomRandomView(generics.ListAPIView):
    queryset = Idiom.objects.order_by('?')[:1]
    serializer_class = IdiomSerializer