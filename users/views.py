from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from users.models import Person


def index(request):
    person = None
    if isinstance(request.user, User) and request.user.is_authenticated():
        person = Person.objects.get(user=request.user)
    context = {'person': person}
    return render(request, 'users/index.html', context)


def action_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
    return redirect('index')


def action_logout(request):
    logout(request)
    return redirect('index')


def change_password(request):
    if request.method == "POST":
        user = request.user
        user.set_password(request.POST['new_password1'])
        user.save()
        update_session_auth_hash(request, user)  # don't logout the user.
    return redirect('profile')
