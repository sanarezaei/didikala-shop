from django.shortcuts import render, redirect
from django.http import request, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from .forms import LoginForm, RegisterForm
from .models import UserProfile

def login_user(request):
    url = request.META.get('HTTP_REFERER')
    form = LoginForm(request.POST or None)
    context = { 'form': form }
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            # redirect to next page or home page after login
            request.session['variantid'] = request.POST
            return HttpResponseRedirect(request.GET.get(
                'next', reversed('home')
                ))
        else:
            form.add_error('username', 'نام کاربری یا کلمه عبور اشتباه میباشد!')
    return render(request, 'accounts/login.html', context)
            
def register(request):
    # if request.user.is_authenticated:
    #     return redirect('')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        username = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user = User.objects.create_user(
            username=username, email=email, password=password
            )
        login(request, user)
        current_user = request.user 
        data = UserProfile()
        data.user_id = current_user.id 
        data.image = "users/image/avatar.png"
        data.save()
        return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    context = {
        'register_form': register_form
    }
    return render(request, "accounts/register.html", context)

def logout(request):
    logout(request)
    return redirect('/')