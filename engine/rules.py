"""
    This dictionary contains the rules for each website. It dictates what class
    names will get what data from a certain website.
"""
RULES = {
    'http://allrecipes.com': {
        'RECIPE_URL': 'http://allrecipes.com/recipe/',
        'INGREDIENTS': ['recipe-ingred_txt'],
        'IMAGE_URL': {'itemprop': 'image'},
        'TITLE': ['recipe-summary__h1'],
        'DIRECTIONS': ['recipe-directions']
    },
    'http://foodnetwork.com': {
        'RECIPE_URL': 'http://www.foodnetwork.com/recipes/',
        'INGREDIENTS': ['ingredients box-block'],
        'TITLE': ['tier-3 title'],
        'DIRECTIONS': ['directions']
    },
    'http://www.simplyrecipes.com': {
        'RECIPE_URL': 'http://www.simplyrecipes.com/recipes/',
        'INGREDIENTS': ['ingredient'],
        'IMAGE_URL': ['photo'],
        'TITLE': ['entry-title'],
        'DIRECTIONS': ['instructions']
    }
}

# If the ingredient contains any of these words, don't add it to the list
BAD_INGREDIENTS = [
    'ingredient',
    'advertisement'
]
