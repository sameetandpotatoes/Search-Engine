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

def get_html(base, level):
    if level < 0 or base is None or not(validators.url(base)):
        return

    print "URL: {} Level: {}".format(base, level)
    r = requests.get(base)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Do any parsing on current url
    parent_url = url_in_rules(base)
    if parent_url is not None:
        ingredients = soup(attrs={'class':rules.RULES[parent_url]['INGREDIENTS']})
        if len(ingredients) is not 0:
            for ing in ingredients:
                print(ing)
    # Now loop through all linked pages on the page and get their content too
    for link in soup.find_all('a'):
        page_url = link.get('href')
        if page_url is None or page_url is '' or page_url is '/' or page_url is base or validators.url(page_url):
            continue
        else:
            page_url = urljoin(base, page_url)
            get_html(page_url, level - 1)

get_html('http://allrecipes.com/', 2)
