from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Hotel Room Management"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to the Hotel Room Management Portal"

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URLs
    path('', include('home.urls')),   # Include URLs from the 'home' app
]
