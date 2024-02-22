from django import forms
import string
import random
from .models import Paper, Author

def id_gen():
    res = ''.join(random.choices(string.ascii_letters, k=10))
    return str(res)

class PaperForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class':"form-control"}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class':"form-control"}))
    publication_date = forms.DateField(label="Date of Publish", widget=forms.DateInput(attrs={'type': 'date','class':"form-control"}))
    publication = forms.CharField(label="Publication", widget=forms.TextInput(attrs={'class':"form-control"}))
    doi = forms.CharField(label="DOI", widget=forms.TextInput(attrs={'class':"form-control"}))
    citation = forms.FloatField(label="Citation", widget=forms.NumberInput(attrs={'class':"form-control",'step': 0.1}))
    impact_factor = forms.FloatField(label="Impact Factor", widget=forms.NumberInput(attrs={'class':"form-control",'step': 0.1}))
    
    class Meta:
        model = Paper
        fields = ['id', 'title','description','publication_date','publication','doi','citation','impact_factor']
    
class AuthorForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))
    profile = forms.URLField(label="Profile", widget=forms.URLInput(attrs={'class':"form-control", 'id':id_gen()}))
    phone = forms.IntegerField(label="Phone Number", widget=forms.NumberInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))
    
    class Meta:
        model = Author
        fields = ['id','first_name','last_name','email','profile','phone']