from django.shortcuts import render, HttpResponse
from .forms import PaperForm, AuthorForm
from .models import Paper, Author
from django.contrib.auth.decorators import login_required

def papers(request):
    return render(request, 'paper.html', {})

@login_required
def addPaper(request):
    paper = PaperForm()
    author = AuthorForm()
    context = {'paperForm':paper, "authorForm":author}
    return render(request, 'addPapers.html',context)

@login_required
def savePaper(request):
    if request.method == 'POST':
        #var = request.POST.getlist("first_name")
        title = request.POST["title"]
        description = request.POST["description"]
        publication_date = request.POST["publication_date"]
        publication = request.POST["publication"]
        doi = request.POST["doi"]
        citation = request.POST["citation"]
        impact_factor = request.POST["impact_factor"]
        try:
            paper = Paper(title=title,description=description,
                          publication_date=publication_date,
                          publication=publication,doi=doi,
                          citation=citation,impact_factor=impact_factor)
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
                author = Author(first_name=first_name[count],last_name=last_name[count],
                                email=email[count], profile=profile[count],
                                phone=phone[count],paper=paper,author_type=author_type)
                print(author.paper.pk)
                author.save()
        except Exception as e:
            return HttpResponse("Error: "+e+"\n <input type=button value=\"Previous Page\" onClick=\"javascript:history.go(-1);\">")
    return HttpResponse("<input type=button value=\"Previous Page\" onClick=\"javascript:history.go(-1);\">")