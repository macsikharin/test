from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

def index(request):
    id = '001'
    name = 'Somchai'
    email = 'somchai@mail.com'

    activities = [
        'Football',
        'Running',
        'Badminton',
    ]

    return render(request, 'index.html', {
        'id': id,
        'name': name,
        'email': email,
        'activities': activities,
    })


def hello(request, id):
    return HttpResponse('Hello World Id=' + str(id))


def article(request, year, slug):
    return HttpResponse('Article Year=' + str(year) + ' Slug=' + slug)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book:index')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {
        'form': form,
    })


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('myapp:index')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book:index')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {
        'form': form,
    })
