from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name="paper"),
    path('add',views.addPaper,name="addpaper"),
]