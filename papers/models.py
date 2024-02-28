from django.db import models
    
class Paper(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField(null=False, blank=False)
    publication = models.CharField(null=False, blank=False)
    doi = models.URLField(null=True, blank=True)
    citation = models.FloatField(null=True, blank=True)
    impact_factor = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.title + ' | ' + self.publication
    def get_publication_date(self):
        from datetime import datetime # idk if this is required, I assume so?
        return self.publication_date.strftime("%d-%b-%Y")
    
    class Meta:
        ordering = ('-date_created',)
    
class Author(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(null=False, blank=False)
    last_name = models.CharField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profile = models.URLField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE,null=False, blank=False)
    author_type_choices = {
        "FIRST":"First Author",
        "CO":"Co-Author"
    }
    author_type = models.CharField(max_length=9,
                  choices=author_type_choices,
                  default="CO")
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' | ' + self.author_type_choices[self.author_type]
    
    class Meta:
        ordering = ('date_created',)