from engine.highlighter import MyHighlighter

"""
Helper method that adds html to any query that appears
"""
def highlight(query, text):
    h = MyHighlighter(query)
    highlighted_text = h.highlight(text)
    return highlighted_text
