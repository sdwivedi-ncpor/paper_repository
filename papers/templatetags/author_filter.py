from django import template

register = template.Library()

@register.filter
def author_filter(paper, author):
    return author.filter(paper=paper)

@register.filter
def author_first_filter(author, paper):
    return author.filter(paper=paper).filter(author_type="FIRST")