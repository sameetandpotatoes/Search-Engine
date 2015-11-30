from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image_url = models.TextField(max_length=2000)
    recipe_url = models.TextField(max_length=2000, unique=True)

    def __str__(self):
    	return self.title

class Ingredient(models.Model):
    title = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe)

    class Meta:
        unique_together = ('title', 'recipe',)

    def __str__(self):
    	return self.title
