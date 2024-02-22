from django.shortcuts import render
from papers.models import Paper, Author

def homepage(request):
    papers = Paper.objects.count()
    publication = Paper.objects.values('publication').distinct().count()
    author = Author.objects.values('email').distinct().count()
    context = {"papers":papers,"publications":publication, "authors":author}
    return render(request,"home.html",context)

def custom_500(request):
    return render(request, '500.html', status=500)