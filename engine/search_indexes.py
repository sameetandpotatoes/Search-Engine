import datetime
from haystack import indexes
from models import Recipe, Ingredient

class RecipeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return Recipe

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

class IngredientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    recipe = indexes.CharField(model_attr='recipe')
    def get_model(self):
        return Ingredient

    # def index_queryset(self, using=None):
    #     """Used when the entire index for model is updated."""
    #     return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())
