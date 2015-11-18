from bs4 import BeautifulSoup
import requests
import IPython
import validators
import rules
from urlparse import urljoin
from models import Recipe, Ingredient

"""
    Helper function that returns the base website of a specific url if it is a
    recipe, or None if
"""
def url_in_rules(url):
    for key, value in rules.RULES.iteritems():
        if value["RECIPE_URL"] in url:
            return key
    return None

"""
    Get the ingredients from a url, formatted in a list
"""
def filter_ingredients(parent_url, soup):
    good_ingredients = []
    for ing in soup(attrs={'class':rules.RULES[parent_url]['INGREDIENTS']}):
        trimmed_ingredient = ing.getText().encode('ascii','ignore')
        if not(any(i in trimmed_ingredient for i in rules.BAD_INGREDIENTS)) and trimmed_ingredient:
            good_ingredients.append(trimmed_ingredient)
    return good_ingredients

"""
    Get the title of the recipe from a url
"""
def get_title_from_page(parent_url, soup):
    title = soup(attrs={'class':rules.RULES[parent_url]['TITLE']})
    if title is None or len(title) == 0:
        return None
    else:
        return title[0].getText().encode('ascii','ignore')

"""
    Get image of the recipe from a url
"""
def get_image_from_page(parent_url, soup):
    image_url = soup(attrs=rules.RULES[parent_url]['IMAGE_URL'])
    if image_url is None or len(image_url) == 0:
        return None
    else:
        return image_url[0]['src']

"""
    Recursive web crawler that gets the data from a base_url
"""
def get_html(base, level):
    # Base case
    if level < 0 or base is None or not(validators.url(base)):
        return

    r = requests.get(base)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Do any parsing on current url
    parent_url = url_in_rules(base)
    if parent_url is not None:
        ingredients = filter_ingredients(parent_url, soup)
        title = get_title_from_page(parent_url, soup)
        image_url = get_image_from_page(parent_url, soup)
        if not(title is None or image_url is None):
            recipe, created = Recipe.objects.get_or_create(
                title=title,
                image_url=image_url,
                recipe_url=base
            )
            # If a new one had to be created, save it in the database
            if created:
                print("Adding recipe: {}".format(title))
                recipe.save()

            for i in ingredients:
                ingredient, created = Ingredient.objects.get_or_create(
                    title=i,
                    recipe=recipe
                )
                if created:
                    print("Adding ingredient: {}".format(i))
                    ingredient.save()

    # Now loop through all linked pages on the page and get their content too
    for link in soup.find_all('a'):
        page_url = link.get('href')
        if page_url is None or page_url == '' or page_url == '/' or page_url == base or validators.url(page_url):
            continue
        else:
            page_url = urljoin(base, page_url)
            get_html(page_url, level - 1)
