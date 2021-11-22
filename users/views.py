from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
def register (request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('first_name')+" "+form.cleaned_data.get('last_name')
            messages.success(request, f"Account created for {name}!")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request,'users/register.html',{'form': form})
@login_required
def profile (request):
    return render(request,'users/profile.html')