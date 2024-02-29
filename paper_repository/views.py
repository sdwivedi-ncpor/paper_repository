from django.shortcuts import render
from papers.models import Paper, Author
from django.db.models import Value as V
from django.db.models.functions import Concat

def homepage(request):
    publications = Paper.objects.values('publication').distinct().order_by('publication')
    publication_list = []
    for pub in publications:
        publication_list.append(pub)
    papers = Paper.objects.count()
    publication = Paper.objects.values('publication').distinct().count()
    author = Author.objects.values('email').distinct().count()
    authors = Author.objects\
        .annotate(full_name=Concat('first_name', V(' '), 'last_name')).values('full_name').distinct().order_by('full_name')
    author_list = []
    for auth in authors:
        author_list.append(auth)
    context = {"papers":papers,"publications":publication, "authors":author,"publication_list":publication_list,"author_list":author_list}
    return render(request,"home.html",context)

def custom_500(request):
    return render(request, '500.html', status=500)