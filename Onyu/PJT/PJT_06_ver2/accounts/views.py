from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import CustomUserCreationForm

# Create your views here.
@require_http_methods(['POST', 'GET'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
        
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)

def login(request):
    pass


def logout(request):
    pass