from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.TextField(max_length=2000)

class Ingredients(models.Model):
    title = models.CharField(max_length=30)
