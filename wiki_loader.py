import wikipedia

def parse(article_name):
    page = wikipedia.page(article_name, auto_suggest = False)
    return page.content
    
if __name__ == "__main__":
    print(parse("Karl Marx"))
