from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def user_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == "Admin":
                return redirect('home')
            else:
                return redirect('user_homepage')
        else:
            return redirect('login')
    
    return wrapper