from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from haystack.query import SearchQuerySet
from haystack.inputs import Raw
from engine import utils
from engine.models import Recipe, Ingredient
import json
import IPython
import utils
import timeit

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

    start_time = timeit.default_timer()

    # Exact match
    indexed_results = SearchQuerySet().auto_query(query).load_all()

    query = query.replace('"', '') # Remove quotes from the query, so highlighting works

    # Partial match
    if not(indexed_results):
        indexed_results = SearchQuerySet().filter(text=Raw("*" +  query + "*"))

    begin = ((page - 1) * RESULTS_PER_PAGE)
    end = begin + RESULTS_PER_PAGE

    results = {}
    ingredients = []
    recipes = []

    if end < len(indexed_results):
        results['next'] = '/recipes?q={}&page={}'.format(query, page + 1)
    if page != 1:
        results['previous'] = '/recipes?q={}&page={}'.format(query, page - 1)

    list_of_recipe_indices = range(begin, end)

    for recipe_num in list_of_recipe_indices:
        if recipe_num >= len(indexed_results):
            results.pop('next', None)
            break
        result = indexed_results[recipe_num]
        recipe_model = result.object if isinstance(result.object, Recipe) else result.object.recipe
        recipe_model.title = utils.highlight(query, recipe_model.title)
        duplicate = False
        for x in recipes:
            if x['title'] == recipe_model.title:
                duplicate = True
                list_of_recipe_indices.append(list_of_recipe_indices[-1] + 1)
                break
        if duplicate: continue

        recipe = {}
        recipe['title'] = recipe_model.title
        recipe['image_url'] = recipe_model.image_url
        recipe['url'] = recipe_model.recipe_url
        recipe['ingredients'] = [utils.highlight(query, t.title) for t in Ingredient.objects.filter(recipe=recipe_model).all()]
        recipes.append(recipe)

    elapsed = timeit.default_timer() - start_time

    results['total'] = len(recipes)
    results['elapsed'] = round(elapsed, 4)
    results['recipes'] = recipes
    results['per_page'] = RESULTS_PER_PAGE
    return HttpResponse(json.dumps(results), content_type='application/json')
