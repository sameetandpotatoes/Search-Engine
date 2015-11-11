from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=30, unique=True)
    image_url = models.TextField(max_length=2000)
    recipe_url = models.TextField(max_length=2000, unique=True)

class Ingredients(models.Model):
    title = models.CharField(max_length=30, unique=True)
    recipe = models.ForeignKey(Recipe)
