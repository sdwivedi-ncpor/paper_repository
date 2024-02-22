from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import PaperForm, AuthorForm
from .models import Paper, Author
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def papers(request):
    paper = Paper.objects.all()
    authors = Author.objects.all()
    context = {"papers": paper, "authors":authors}
    return render(request, 'paper.html', context)

def paperDetails(request, pk):
    paper = Paper.objects.get(pk=pk)
    authors = Author.objects.filter(paper=paper)
    context={"paper":paper, "authors":authors}
    return render(request, "paperdetails.html", context)


@login_required
def formPaper(request, id=None):
    if request.POST:
        paperform = PaperForm(request.POST)
        authorform = [AuthorForm(request.POST)]
    else:
        if id:
            paper = get_object_or_404(Paper, pk=id)
            author = Author.objects.filter(paper=paper)
            paperform = PaperForm(instance=paper)
            authorform = []
            for auth in author:
                authorform.append(AuthorForm(instance=auth))
        else:
            paperform = PaperForm(instance=Paper())
            authorform = [AuthorForm(instance=Author())]
    sample_author_form = AuthorForm()
    context = {'paperForm':paperform, "authorForm":authorform,"sample_author_form":sample_author_form}
    return render(request, 'addPapers.html',context)

@login_required
def savePaper(request):
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        publication_date = request.POST["publication_date"]
        publication = request.POST["publication"]
        doi = request.POST["doi"]
        citation = request.POST["citation"]
        impact_factor = request.POST["impact_factor"]
        id = request.POST.getlist('id')
        try:
            if id[0] is '':
                paper = Paper(title=title,description=description,
                          publication_date=publication_date,
                          publication=publication,doi=doi,
                          citation=citation,impact_factor=impact_factor)
            else:
                p = Paper.objects.get(pk=id[0])
                paper = Paper(pk=id[0],date_created=p.date_created,title=title,description=description,
                            publication_date=publication_date,
                            publication=publication,doi=doi,
                            citation=citation,impact_factor=impact_factor)
            id.pop(0)
            paper.save()
            first_name = request.POST.getlist("first_name")
            last_name = request.POST.getlist("last_name")
            email = request.POST.getlist("email")
            profile = request.POST.getlist("profile")
            phone = request.POST.getlist("phone")
            for count in range(0,len(first_name)):
                author_type = "CO"
                if count==0:
                    author_type = "FIRST"
                if id[count] is '':
                    author = Author(first_name=first_name[count],last_name=last_name[count],
                                email=email[count], profile=profile[count],
                                phone=phone[count],paper=paper,author_type=author_type)
                else:
                    a = Author.objects.get(pk=id[count])
                    author = Author(pk = id[count],date_created=a.date_created,first_name=first_name[count],last_name=last_name[count],
                                email=email[count], profile=profile[count],
                                phone=phone[count],paper=paper,author_type=author_type)
                author.save()
        except Exception as e:
            return HttpResponse(e.with_traceback())
        return redirect(reverse('paperdetails', kwargs={'pk' : paper.pk}))
    else:
        return redirect('/')
    #return HttpResponse("<input type=button value=\"Previous Page\" onClick=\"javascript:history.go(-1);\">")

def deleteAuthor(request,pk):
    if Author.objects.filter(pk=pk).exists():
        author = Author.objects.get(pk=pk)
        author.delete()
        return HttpResponse("Deleted")
    else:
        return HttpResponse(status=500)
    
def searchfun(request, search):
    queryset = Paper.objects.filter(publication__icontains=search)
    return HttpResponse(queryset)