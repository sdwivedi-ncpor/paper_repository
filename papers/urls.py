from django.urls import path
from . import views

urlpatterns = [
    path('',views.papers,name="paper"),
    path('add',views.formPaper,name="addpaper"),
    path('edit/<int:id>',views.formPaper,name="editpaper"),
    path('save',views.savePaper,name="savepaper"),
    path('<int:pk>', views.paperDetails, name="paperdetails"),
    path('delete/<int:pk>', views.deleteAuthor, name="deleteauthor"),
    path('search/<str:search>', views.searchfun, name="search"),
    path('import', views.importfile, name="importfile"),
    path('pub', views.publicationpage, name="publicationpage"),
    path('auth', views.authorpage, name="authorpage"),
]