from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_get(request):
    context = {
        'next': request.GET.get("next", 'profile')
    }
    return render(request, 'home.html', context)


def login_post(request):
    context = dict()
    resolve_url = request.GET.get("next")
    username = request.POST.get('username')
    password = request.POST.get('password')
    user: User = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        groups = list(user.groups.all())
        request.session.__setattr__("groups", groups)
        return redirect(resolve_url)
    else:
        context['message'] = 'username or password incorrect'
        return render(request, 'home.html', context)


def log_out(request):
    logout(request)
    return redirect("home")


def change_password(request, user_id: int):
    pass
