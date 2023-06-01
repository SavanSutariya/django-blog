from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
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
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance= request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account is updated successfully")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance= request.user.profile)
        c_user = request.user
        posts = c_user.post_set.all()
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': posts
    }
    return render(request,'users/profile.html',context)