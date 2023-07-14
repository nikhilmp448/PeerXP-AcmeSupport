from django.shortcuts import render
from ticket.Zenpy import zenpy_client
from django.shortcuts import redirect
from user.forms import  CreateTicket
from zenpy.lib.api_objects import Ticket, User,CustomField
from django.contrib import messages

# CREATE
def create_ticket(request):
    form = CreateTicket(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print('valid')
            Email = form.cleaned_data['email']
            Phone = form.cleaned_data['Phone_Number']
            Description = form.cleaned_data['description']
            Subject = form.cleaned_data['subject']
            Priority = form.cleaned_data['priority']
            
            """
            Zendesk create ticket API call .."""
            
            zenpy_client.tickets.create(
            Ticket(description=Description,subject=Subject,priority=Priority,custom_fields=[CustomField(id=6946196446109, value=Email),CustomField(id=6946196963741, value=Phone)],
                requester=User(name=request.user.name, email=request.user.email)))
            
        messages.success(request,"Ticket Submitted Successfuly")
            
        return redirect('user_homepage')
    return redirect('login')

# DELETE
def delete_ticket(request,id):
    tickets = zenpy_client.tickets()

    for ticket in tickets:
        if ticket.id ==id:          
            zenpy_client.tickets.delete(ticket)
            
    if request.user.is_admin:
        return redirect('list')
    
    return redirect('tickets')

# VIEW
def lists(request):
    tickets = zenpy_client.tickets()
    my_tickets=[]
    
    for ticket in tickets:
        my_tickets.append(ticket.to_dict()) 
    context = {'p':my_tickets}
    
    return render(request,'list.html', context)

