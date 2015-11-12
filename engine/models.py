from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=30, unique=True)
    image_url = models.TextField(max_length=2000)
    recipe_url = models.TextField(max_length=2000, unique=True)

    def __str__(self):
    	return self.title

class Ingredients(models.Model):
    title = models.CharField(max_length=30, unique=True)
    recipe = models.ForeignKey(Recipe)

    def __str__(self):
    	return self.title
