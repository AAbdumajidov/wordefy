from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:list')
    context = {
        'form': form
    }
    return render(request, 'profile/login.html', context)


def logout_view(request):   
    if not request.user.is_anonymous:
        if request.method == "POST":
            logout(request)
            return redirect('blog:index')
    else:
        return redirect('profile/logout.html')

    return render(request, 'profile/logout.html')


def register_view(request):
    if not request.user.is_anonymous:
        return redirect('blog:list')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('accaunt:login')
    context = {
        'form': form
    }
    return render(request, 'profile/register.html', context)