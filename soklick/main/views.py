from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from main.forms import LinksUser
from main.models import LinksUsers

def home(request):
    
    data = {
        'title': 'Главная'
    }

    return render(
        request = request,
        template_name = 'main/home.html',
        context = data
    )

def about(request):

    data = {
        'title': 'О нас'
    }

    return render(
        request = request,
        template_name = 'main/about.html',
        context = data
    )

def links(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['user'] = request.user
        request.POST = post

        form = LinksUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('links')
    else:
        form = LinksUser()

    links = LinksUsers.objects.filter(user = request.user)
    data = {
        'title': 'Ссылки',
        'form': form,
        'links': links
    }

    return render(
        request = request,
        template_name = 'main/links.html',
        context = data
    )