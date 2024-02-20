from django.shortcuts import render
from papers.models import Paper, Author

def homepage(request):
    papers = Paper.objects.count()
    publication = Paper.objects.values('publication').distinct().count()
    author = Author.objects.values('email').distinct().count()
    context = {"papers":papers,"publications":publication, "authors":author}
    return render(request,"base.html",context)