import wikipedia

def parse(article_name):
    page = wikipedia.page(article_name, auto_suggest = False)
    return page.content
