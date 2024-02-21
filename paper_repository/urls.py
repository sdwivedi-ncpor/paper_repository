"""
URL configuration for paper_repository project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from papers import urls as paperurls
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from .forms import UserLoginForm, UserPassworChangeForm
from django.contrib.auth import views as authview
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [    
    path('accounts/login/',
         authview.LoginView.as_view(template_name="registration/login.html",
                                    authentication_form=UserLoginForm),
         name='login'),
    path('accounts/password_change/',
         login_required(authview.PasswordChangeView.as_view(template_name="registration/password_change_form.html",
                                             form_class=UserPassworChangeForm)),
         name='password_change'),
    path(
        "password_change/done/",
        login_required(authview.PasswordChangeDoneView.as_view()),
        name="password_change_done",
    ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',views.homepage,name="homepage"),
    path('paper/', include(paperurls)),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.png')))
]

admin.site.site_header = settings.ADMIN_SITE_HEADER