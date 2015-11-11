from bs4 import BeautifulSoup
import requests
import IPython
import validators
import rules
from urlparse import urljoin


def url_in_rules(url):
    for key, value in rules.RULES.iteritems():
        if value["RECIPE_URL"] in url:
            return key
    return None

def filter_ingredients(parent_url, soup):
    good_ingredients = []
    for ing in soup(attrs={'class':rules.RULES[parent_url]['INGREDIENTS']}):
        trimmed_ingredient = ing.getText()
        if not(any(i in trimmed_ingredient for i in rules.BAD_INGREDIENTS)) and trimmed_ingredient:
            good_ingredients.append(trimmed_ingredient)
    return good_ingredients

def get_title_from_page(parent_url, soup):
    return soup(attrs={'class':rules.RULES[parent_url]['TITLE']})[0].getText()

def get_html(base, level):
    if level < 0 or base is None or not(validators.url(base)):
        return

    print "URL: {} Level: {}".format(base, level)
    r = requests.get(base)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Do any parsing on current url
    parent_url = url_in_rules(base)
    if parent_url is not None:
        ingredients = filter_ingredients(parent_url, soup)
        title = get_title_from_page(parent_url, soup)
        print "{}: {}".format(title, ingredients)
    # Now loop through all linked pages on the page and get their content too
    for link in soup.find_all('a'):
        page_url = link.get('href')
        if page_url is None or page_url is '' or page_url is '/' or page_url is base or validators.url(page_url):
            continue
        else:
            page_url = urljoin(base, page_url)
            get_html(page_url, level - 1)

get_html('http://allrecipes.com/recipe/234803/chef-johns-smothered-pork-chops/', 2)
