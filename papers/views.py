from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import PaperForm, AuthorForm
from .models import Paper, Author
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Value as V
from django.db.models.functions import Concat

def papers(request):
    title = request.GET.get('title',"")
    publication = request.GET.get('publication',"")
    author = request.GET.get('author',"")
    author_type = request.GET.get('author_type', "")
    if author_type == "ANY":
        author_type = ""
    authors_list = Author.objects\
        .annotate(full_name=Concat('first_name', V(' '), 'last_name'))\
        .filter(full_name__icontains=author)\
        .filter(author_type__icontains=author_type).order_by('-date_created')
    paper_id = []
    for auth in authors_list:
        paper_id.append(auth.paper.pk)
    paper_obj = Paper.objects\
        .filter(pk__in=paper_id)\
        .filter(title__icontains=title)\
        .filter(publication__icontains=publication)\
        .order_by("publication")\
        .order_by('-date_created')
    authors = Author.objects.all()
    paginator = Paginator(paper_obj, 10)
    page_number = request.GET.get("page")
    paper = paginator.get_page(page_number)
    context = {"papers": paper, "authors":authors, "title":title, "publication":publication, "author":author, "author_type":author_type}
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
            if id[0] == '':
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
                if id[count] == '':
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

@login_required
def importfile(request):
    if request.method == 'POST':
        messages.warning(request, "Your account expires in three days.")
        messages.error(request, "Error. Message not sent.")
    context={}
    return render(request, 'import.html',context)

def publicationpage(request):
    publications = Paper.objects.values('publication').distinct().order_by('publication')
    publication = []
    for pub in publications:
        publication.append(pub)
    pub_search = request.GET.get('pub_search','')
    paper_obj = Paper.objects.filter(publication__icontains=pub_search)
    author = Author.objects.all()
    paginator = Paginator(paper_obj, 10)
    page_number = request.GET.get("page")
    paper = paginator.get_page(page_number)
    context = {"publication":publication, 'papers': paper, 'authors':author}
    return render(request, 'publication.html', context)

def authorpage(request):
    authors = Author.objects\
        .annotate(full_name=Concat('first_name', V(' '), 'last_name')).values('full_name').distinct().order_by('full_name')
    author_list = []
    for auth in authors:
        author_list.append(auth)
    auth_search = request.GET.get('auth_search','')
    authors_first_list = Author.objects\
        .annotate(full_name=Concat('first_name', V(' '), 'last_name'))\
        .filter(full_name__icontains=auth_search)\
        .filter(author_type__icontains="FIRST").order_by('-date_created')
    paper_f_id = []
    for auth in authors_first_list:
        paper_f_id.append(auth.paper.pk)
    paper_first_obj = Paper.objects.filter(pk__in=paper_f_id)    
    paginator = Paginator(paper_first_obj, 5)
    page_number_f = request.GET.get("page_f")
    paper_first = paginator.get_page(page_number_f)    
    authors_co_list = Author.objects\
        .annotate(full_name=Concat('first_name', V(' '), 'last_name'))\
        .filter(full_name__icontains=auth_search)\
        .filter(author_type__icontains="CO").order_by('-date_created')
    paper_c_id = []
    for auth in authors_co_list:
        paper_c_id.append(auth.paper.pk)
    paper_co_obj = Paper.objects.filter(pk__in=paper_c_id)
    paginator = Paginator(paper_co_obj, 5)
    page_number_c = request.GET.get("page_c")
    paper_co = paginator.get_page(page_number_c)
    author = Author.objects.all()
    context = {"author_list":author_list, 
        'paper_first': paper_first,
        'paper_co':paper_co, 'authors':author,
        'page_number_f':page_number_f,
        'page_number_c':page_number_c}
    return render(request, 'author.html', context)