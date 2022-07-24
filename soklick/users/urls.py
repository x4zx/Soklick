"""soklick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from main import views as MainViews
from . import views as UsersViews
from django.contrib.auth import views as AuthViews

urlpatterns = [
    path('', MainViews.home, name = 'home'),
    path('registration/', UsersViews.registration, name = 'registration'),
    path('authorization/', AuthViews.LoginView.as_view(template_name = 'users/authorization.html'), name = 'authorization'),
    path('exit/', AuthViews.LogoutView.as_view(template_name = 'users/exit.html'), name = 'exit'),
    path('profile/', UsersViews.profile, name = 'profile'),
]
