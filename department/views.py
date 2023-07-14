from django.shortcuts import render,redirect
from user.forms import CreateDepartment
from django.contrib import messages
from user.models import Account

from department.models import Department

# Create your views here.

def create_department(request):
    user = request.user
    form = CreateDepartment(request.POST)
    if request.method == "POST":
        if form.is_valid():
            department = form.save(commit=False)
            department.Created_by = user
            department.save()
            return redirect('home')
        else:
            messages.error(request,'field error')
    context={'form':form}
    return render(request,'create_dep.html',context)



def delete_department(request,id):
    department = Department.objects.filter(id=id)
    print(department)    
    department_users = Account.objects.filter(Department_id=id).exists()
    print(department_users)
    if department_users:
        messages.error(request, "Delete Error : Department associated with some user")
        return redirect('home')
    else :
        department.delete()  
    return redirect('home')
    

def update_department(request,id):
    department = Department.objects.filter(id=id).first()
    form = CreateDepartment(instance=department)
    if request.method == "POST":
        form = CreateDepartment(request.POST,instance=department)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form,'department':department}
    return render(request,'create_dep.html',context)
