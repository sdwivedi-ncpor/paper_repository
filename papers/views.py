from django.shortcuts import render
from .forms import createPaper
# Create your views here.

def login(request):
    return render(request, 'paper.html', {})

def addPaper(request):
    form = createPaper()
    context = {'form':form}
    return render(request, 'addPapers.html',context)