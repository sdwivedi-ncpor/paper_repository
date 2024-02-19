from django import forms

class createPaper(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    publication_date = forms.DateField()
    publication = forms.CharField()
    doi = forms.CharField()
    citation = forms.FloatField()
    impact_factor = forms.FloatField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    profile = forms.URLField()
    phone = forms.IntegerField()