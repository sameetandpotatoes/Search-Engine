"""
Gonna need a dictionary mapping urls to class names for how to get certain things from each website
"""
RULES = {
    'http://allrecipes.com': {
        'RECIPE_URL': 'http://allrecipes.com/recipe/', #If a url doesn't match this, skip?
        'INGREDIENTS': ['checklist', 'dropdownwrapper'],
        'DIRECTIONS': 'recipe-directions'
    }
}
