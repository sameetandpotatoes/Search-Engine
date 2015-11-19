from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from haystack.query import SearchQuerySet
from engine import utils
from engine.models import Recipe, Ingredient
import json
import IPython

RESULTS_PER_PAGE = 10

def home(request):
    base_url = request.build_absolute_uri('/')[:-1]
    return render_to_response('home.html', {
        'base_url': base_url
    })

def get(request):
    utils.get_html("http://allrecipes.com", 2)

def search(request):
    query = request.GET['q']
    page = request.GET.get('page', 1)
    page = int(page)
    page = 1 if page <= 0 else page

    exact_words = query.split('"')

    if len(exact_words) > 1:
        exact_match = exact_words[1]
        indexed_results = SearchQuerySet().boost(exact_match, 3.0).filter(content=query)
    else:
        indexed_results = SearchQuerySet().filter(content=query)

    # Suggest something else if no results were found
    if not(indexed_results):
        sqs = SearchQuerySet().auto_query(query)
        return HttpResponse(json.dumps(sqs.spelling_suggestion(), content_type='application/json'))

    begin = ((page - 1) * RESULTS_PER_PAGE)
    end = begin + RESULTS_PER_PAGE

    results_on_page = indexed_results[begin:end]

    results = {}
    ingredients = []
    recipes = []
    for result in results_on_page:
        recipe_model = result.object if isinstance(result.object, Recipe) else result.object.recipe
        recipe = {}
        recipe['title'] = recipe_model.title
        recipe['image_url'] = recipe_model.image_url
        recipe['url'] = recipe_model.recipe_url
        recipe['ingredients'] = [t.title for t in Ingredient.objects.filter(recipe=recipe_model).all()]
        recipes.append(recipe)
    results['recipes'] = recipes
    if end < len(indexed_results):
        results['next'] = '/recipes?q={}&page={}'.format(query, page + 1)
    if page != 1:
        results['previous'] = '/recipes?q={}&page={}'.format(query, page - 1)
    return HttpResponse(json.dumps(results), content_type='application/json')
