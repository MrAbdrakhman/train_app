# api/serializers.py

from rest_framework import serializers
from .models import Category, Quote, Word, Idiom

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'

class IdiomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idiom
        fields = '__all__'
