from django.shortcuts import render, redirect
from .forms import Login
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    form = Login(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'login.html', {'form': form})

def login_artista(request):
    form = Login(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'login_artista.html', {'form': form})

def login_produtor(request):

    form = Login(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'login_produtor.html', {'form': form})



def tipo(request):
    return render(request, 'tipo.html')


@login_required
def logout(request):
    return render(request, 'logout.html')