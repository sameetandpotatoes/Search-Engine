import datetime
from haystack import indexes
from models import Recipe, Ingredient

class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    image_url = indexes.CharField(model_attr='image_url')
    recipe_url = indexes.CharField(model_attr='recipe_url')
    title = indexes.CharField(model_attr='title', null=True)
    title_auto = indexes.NgramField(model_attr='title')

    def get_model(self):
        return Recipe

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class IngredientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    recipe = indexes.CharField(model_attr='recipe')
    title = indexes.CharField(model_attr='title', null=True)
    title_auto = indexes.NgramField(model_attr='title')

    def get_model(self):
        return Ingredient

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
