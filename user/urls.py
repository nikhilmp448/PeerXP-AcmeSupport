from . import views
from django.urls import path
urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.logout_user,name='logout'),
    
    path('adminhome/',views.admin_home,name='home'),
    path('',views.user_home,name='user_homepage'),
    path('tickets/',views.tickets,name='tickets'),
    path('create_user/',views.create_Adminuser,name='create_user'),

]
