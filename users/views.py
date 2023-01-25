from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import User
# Create your views here.


def main_login_view(request):
    if request.user.is_authenticated:
        return redirect("blog:boardpage")

    if request.method == "POST" and request.POST['id'] and request.POST['password']:

        user_id = request.POST['id']
        user_pw = request.POST['password']

        user = authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            login(request, user)
        else:
            return redirect("users:main_login")

        if request.GET.get('next'):
            next_dest = request.GET.get('next')
            return redirect(next_dest)

        return redirect("blog:boardpage")

    else:
        return render(request, 'users/main_page.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect("users:main_login")


def register_view(request):
    if request.method == "GET":
        return render(request, 'users/register.html')

    elif request.method == "POST":
        new_id = request.POST['username']
        new_email = request.POST['email']
        new_password = request.POST['password']

        # password checking mechanism(?)

        User.objects.create_user(
            username=new_id, email=new_email, password=new_password)

        return redirect("users:main_login")


@login_required
def mypage_view(request):

    return render(request, 'users/mypage.html')
