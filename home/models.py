from django.db import models

class Room(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('maintenance', 'Under Maintenance'),
    ]

    room_id = models.IntegerField(primary_key=True)  # Unique ID for the room
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"Room {self.room_id} - {self.status}"


class Booking(models.Model):
    user_email = models.EmailField()  # User email for booking
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # Link to Room model

    def __str__(self):
        return f"Booking for Room {self.room.room_id} by {self.user_email}"


# after all this 2 cheeZ important to to register the models in admin.py and setting me jake 
# INSTALLED_APPS = [
#     "home.apps.HomeConfig",
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
# ]