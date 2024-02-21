from django import forms
import string
import random

def id_gen():
    res = ''.join(random.choices(string.ascii_letters, k=10))
    return str(res)

class PaperForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'class':"form-control"}))
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'class':"form-control"}))
    publication_date = forms.DateField(label="Date of Publish", widget=forms.DateInput(attrs={'type': 'date','class':"form-control"}))
    publication = forms.CharField(label="Publication", widget=forms.TextInput(attrs={'class':"form-control"}))
    doi = forms.CharField(label="DOI", widget=forms.TextInput(attrs={'class':"form-control"}))
    citation = forms.FloatField(label="Citation", widget=forms.NumberInput(attrs={'class':"form-control",'step': 0.5}))
    impact_factor = forms.FloatField(label="Impact Factor", widget=forms.NumberInput(attrs={'class':"form-control",'step': 0.5}))
    
class AuthorForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))
    profile = forms.URLField(label="Profile", widget=forms.URLInput(attrs={'class':"form-control", 'id':id_gen()}))
    phone = forms.IntegerField(label="Phone Number", widget=forms.NumberInput(attrs={'class':"form-control", 'id':id_gen(), "autocomplete":"on"}))