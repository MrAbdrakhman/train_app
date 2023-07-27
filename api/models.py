from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    translation = models.TextField()

    def __str__(self):
        return self.text

class Idiom(models.Model):
    text = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Word(models.Model):
    text = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

