from django.http import HttpResponse
from django.shortcuts import render_to_response
from haystack.query import SearchQuerySet
from engine import utils
from engine.models import Recipe, Ingredient
import json

def home(request):
    base_url = request.build_absolute_uri('/')[:-1]
    return render_to_response('home.html', {
        'base_url': base_url
    })

def get(request):
    utils.get_html("http://allrecipes.com", 2)

def search(request):
    indexed_results = SearchQuerySet().filter(content=request.GET['q'])
    results = {}
    ingredients = []
    recipes = []
    for result in indexed_results:
        working = result.object
        if isinstance(working, Recipe):
            recipe = {
                'title': working.title,
                'image_url': working.image_url,
                'url': working.recipe_url,
                'ingredients': [t.title for t in Ingredient.objects.filter(recipe=working).all()]
            }
            recipes.append(recipe)
        else:
            ingredient = {
                'title': working.title,
                'recipe': working.recipe.title
            }
            ingredients.append(ingredient)
    results['recipes'] = recipes
    results['bob'] = ingredients
    return HttpResponse(json.dumps(results), content_type='application/json')
