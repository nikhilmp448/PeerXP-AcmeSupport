from department.models import Department
from .forms import  CreateTicket, UserCreationForm
from django.shortcuts import render
from django.contrib import messages , auth
from django.shortcuts import redirect
from user.models import Account
from django.contrib.auth.decorators import login_required
from ticket.Zenpy import zenpy_client
from.decorators import *

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        field = request.POST.get('field')
        password = request.POST.get('password')
        user = auth.authenticate(email=field,password=password)
        
        if not user:
            try:
                user = auth.authenticate(email = Account.objects.get(Phone_Number = field) ,password=password)
            except:
                messages.error(request,"credential wrong")
                
        if user is not None:
            auth.login(request,user)
            if user.is_superadmin or request.user.role == 'Admin':
                return redirect('home')
            return redirect('user_homepage')
        else:
            messages.error(request,"credential wrong")
    return render(request,'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('login')


""" ADMIN DASHBOARD  """

@login_required(login_url='login')
def admin_home(request):
        users = Account.objects.filter(is_superadmin=False)
        department = Department.objects.all()
        context = {'users':users,'department':department}
        return render(request,'home.html',context)
      
     
@login_required(login_url='login')
def create_Adminuser(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('home')
        else:
            print('user is not added')
            messages.info(request,'product not added')
        form = UserCreationForm()
    return render(request,'create_user.html',{'form':form})

""" USER HOME """

@login_required(login_url='login')
def user_home(request):
    user = Account.objects.filter(email= request.user).values('email','Phone_Number')
    form = CreateTicket(user[0])
    context = {'form':form}
    return render (request,'user_homepage.html',context)


@login_required(login_url='login')
def tickets(request):
    tickets=[]
    
    for ticket in zenpy_client.search(type='ticket', requester=request.user.email):
        tickets.append(ticket.to_dict()) 
    print(tickets) 
    context = {
        'tickets':tickets
    }
    return render (request,'tickets.html',context)













    
