from django.contrib import admin
from . import models
from django.contrib.auth.models import Group

admin.site.register(models.Author)
admin.site.register(models.Paper)
admin.site.unregister(Group)