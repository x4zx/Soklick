from django.contrib.auth.decorators import login_required
from .forms import Registration, AccountUpdate
from django.shortcuts import redirect, render
from django.contrib import messages

def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorization')
    else:
        form = Registration()

    return render(
        request = request,
        template_name = 'users/registration.html',
        context = {
            'title': 'Регистрация',
            'form': form
        }
    )

@login_required
def profile(request):
    if request.method == 'POST':
        form = AccountUpdate(
            request.POST,
            instance = request.user
        )

        if form.is_valid():
            form.save()
            messages.success(
                request = request,
                message = 'Ваш аккаунт успешно обновлён!'  
            )
            return redirect('profile')
    else:
        form = AccountUpdate(instance = request.user)

    data = {
        'title': 'Профиль',
        'form': form
    }
    return render(
        request = request,
        template_name = 'users/profile.html',
        context = data
    )