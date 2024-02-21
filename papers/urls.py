from django.urls import path
from . import views

urlpatterns = [
    path('',views.papers,name="paper"),
    path('add',views.addPaper,name="addpaper"),
    path('save',views.savePaper,name="savepaper"),
    path('<int:pk>', views.paperDetails, name="paperdetails"),
]