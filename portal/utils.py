from haystack.utils import Highlighter

"""
Helper method that adds html to any query that appears
"""
def highlight(query, text):
    h = Highlighter(query)
    highlighted_text = h.highlight(text)
    if "..." in highlighted_text:
        return highlighted_text[3:]
    else:
        return highlighted_text
