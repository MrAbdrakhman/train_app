from django.contrib import admin
from .models import Category, Quote, Word, Idiom

admin.site.register(Category)
admin.site.register(Quote)
admin.site.register(Word)
admin.site.register(Idiom)