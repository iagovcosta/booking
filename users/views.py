from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.
@login_required
def new_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'users-form.html', {'form': form})