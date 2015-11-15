from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from haystack.query import SearchQuerySet
from engine import utils
from engine.models import Recipe, Ingredient
import json
import IPython

def home(request):
    return render_to_response('home.html')

def get(request):
    utils.get_html("http://allrecipes.com", 2)

def search(request):
    # results = SearchQuerySet().filter(content=request.GET['q']).models(Recipe)
    #     sqs = SearchQuerySet().auto_query('mor exmples')
    # sqs.spelling_suggestion() # u'more examples'
    indexed_results = SearchQuerySet().filter(content=request.GET['q'])
    results = {}
    ingredients = []
    recipes = []
    for result in indexed_results:
        if result.content_type() == 'engine.ingredient':
            recipe_model = Ingredient.objects.filter(id=result.pk)[0].recipe
        else:
            recipe_model = Recipe.objects.filter(id=result.pk)[0]
        recipe = {}
        recipe['title'] = recipe_model.title
        recipe['image_url'] = recipe_model.image_url
        recipe['url'] = recipe_model.recipe_url
        recipe['ingredients'] = [t.title for t in Ingredient.objects.filter(recipe=recipe_model).all()]
        recipes.append(recipe)
    results['recipes'] = recipes
    return HttpResponse(json.dumps(results), content_type='application/json')
