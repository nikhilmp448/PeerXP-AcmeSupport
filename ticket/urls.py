from . import views
from django.urls import path
urlpatterns = [
    
    path('delete_ticket/<int:id>',views.delete_ticket,name='delete_ticket'),
    path('list/',views.lists,name='list'),
    path('create_ticket',views.create_ticket,name='create_ticket'),

]
