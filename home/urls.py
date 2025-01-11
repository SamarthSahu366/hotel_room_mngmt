from django.urls import path
from . import views

urlpatterns = [
    # For non-admin users where admin authentication is not required
    path('', views.index, name='index'),  # Home page for all users
    path('rooms/avaiblerooms', views.search_available_rooms, name='search_available_rooms'),  # Search available rooms for users
    path('rooms/book', views.bookroom, name='book_room'),  # Book a room
    path('rooms/cancel', views.cancelbooking, name='cancel_booking'),  # Cancel booking

    # For admin users where admin authentication is required
    # path('',views.index),
    path('rooms', views.view_all_rooms, name='admin_view_all_rooms'),
    path('rooms/add', views.addroom, name='admin_add_rooms'),
    path('rooms/update', views.update_room, name='admin_update_room'),
    path('rooms/delete', views.delete_room, name='admin_delete_room'),  # Delete room (admin only)
]
