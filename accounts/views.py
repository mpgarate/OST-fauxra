from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate()
            login(request, new_user)
            return redirect("index")
        else:
            return redirect("index")
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
