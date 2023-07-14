    
from . import views
from django.urls import path
urlpatterns = [
    path('create_department/',views.create_department,name='create_department'),
    path('delete_dep/<int:id>',views.delete_department,name='delete_dep'),
    path('update_dep/<int:id>',views.update_department,name='update_dep'),
    
]
