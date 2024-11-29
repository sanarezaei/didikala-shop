from django.shortcuts import render
from django.http import request, HttpResponseRedirect

from .forms import LoginForm

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
            
