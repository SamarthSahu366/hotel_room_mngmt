from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('viewallrooms/', views.view_all_rooms, name='viewallrooms'),
    path('addroom/', views.addroom, name='addroom'),
    path('updateroom/', views.update_room,name='updateroom'),  
    path('deleteroom/', views.delete_room, name='deleteroom'), 
]
