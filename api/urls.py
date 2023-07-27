
from django.urls import path
from .views import QuoteRandomView, QuoteListCreateView, CategoryListCreateView, WordListCreateView, WordRetrieveView, IdiomRandomView

urlpatterns = [
    path('quote/random/', QuoteRandomView.as_view(), name='quote-random'),
    path('quote/', QuoteListCreateView.as_view(), name='quote-list-create'),
    path('category/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('word/', WordListCreateView.as_view(), name='word-list-create'),
    path('word/<int:pk>/', WordRetrieveView.as_view(), name='word-retrieve'),
    path('idiom/random/', IdiomRandomView.as_view(), name='idiom-random'),

]