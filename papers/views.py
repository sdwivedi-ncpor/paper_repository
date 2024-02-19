from django.shortcuts import render
from .forms import PaperForm, AuthorForm
# Create your views here.

def login(request):
    return render(request, 'paper.html', {})

def addPaper(request):
    paper = PaperForm()
    author = AuthorForm
    context = {'paperForm':paper, "authorForm":author}
    return render(request, 'addPapers.html',context)