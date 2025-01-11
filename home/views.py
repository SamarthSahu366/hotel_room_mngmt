from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from home.models import Room

def is_admin(user):
    return user.is_staff

def index(request):
    return render(request, 'index.html')

def search_available_rooms(request):
    
        rooms = Room.objects.filter(status='available')
        return render(request, 'avaiblerooms.html', {'rooms': rooms})

@login_required(login_url='/login/')
def book_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('roomid')
        user = request.user
        if room_id:
            try:
                room = Room.objects.get(room_id=room_id, status='available')
                room.status = 'booked'
                room.save()
                message = f"Room {room_id} has been successfully booked."
            except Room.DoesNotExist:
                message = f"Room {room_id} is either not available or doesn't exist."
        else:
            message = "Please provide a valid room ID."
        return render(request, 'book_room.html', {'message': message})
    return render(request, 'book_room.html')

@login_required(login_url='/login/')
def cancel_booking(request):
    if request.method == 'POST':
        room_id = request.POST.get('roomid')
        user = request.user
        if room_id:
            try:
                room = Room.objects.get(room_id=room_id, status='booked')
                room.status = 'available'
                room.save()
                message = f"Booking for Room {room_id} has been successfully canceled."
            except Room.DoesNotExist:
                message = f"Room {room_id} was not found or is not currently booked."
        else:
            message = "Please provide a valid room ID."
        return render(request, 'cancel_booking.html', {'message': message})
    return render(request, 'cancel_booking.html')

@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def view_all_rooms(request):
        rooms = Room.objects.all()
        return render(request, 'view_all_rooms.html', {'rooms': rooms})

@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def addroom(request):
    if request.method == "POST":
        room_id = request.POST.get('roomid')
        status = request.POST.get('status')
        if room_id and status:
            room = Room(room_id=room_id, status=status)
            room.save()
            message = "Room successfully added"
        else:
            message = "Please provide all necessary details."
        return render(request, 'addroom.html', {'message': message})
    return render(request, 'addroom.html')

@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def update_room(request):
    if request.method == "POST":
        room_id = request.POST.get('roomid')
        new_status = request.POST.get('status')
        if room_id and new_status:
            try:
                room = Room.objects.get(room_id=room_id)
                old_status = room.status  # Get the current status of the room
                if old_status == new_status:
                    message = f"Room {room_id} status is already '{old_status}'."
                else:
                    room.status = new_status
                    room.save()
                    message = f"Room {room_id} status updated successfully from '{old_status}' to '{new_status}'."
            except Room.DoesNotExist:
                message = f"No room found with ID {room_id}."
        else:
            message = "Please provide both Room ID and Status."
        return render(request, 'update_room.html', {'message': message})
    return render(request, 'update_room.html')
    if request.method == "POST":
        room_id = request.POST.get('roomid')
        new_status = request.POST.get('status')
        if room_id and new_status:
            try:
                room = Room.objects.get(room_id=room_id)
                old_status=room.status
                if old_status==new_status:
                    message='room status is already {old_status}'
                room.status = new_status
                room.save()
                message = f"Room {room_id} status updated successfully to '{new_status}'."
            except Room.DoesNotExist:
                message = f"No room found with ID {room_id}."
        else:
            message = "Please provide both Room ID and Status."
        return render(request, 'update_room.html', {'message': message})
    return render(request, 'update_room.html')

@login_required(login_url='/admin/login/')
@user_passes_test(is_admin, login_url='/admin/login/')
def delete_room(request):
    if request.method == "POST":
        room_id = request.POST.get('roomid')
        if room_id:
            try:
                room = Room.objects.get(room_id=room_id)
                room.delete()
                message = f"Room {room_id} deleted successfully."
            except Room.DoesNotExist:
                message = f"Room {room_id} not found."
        else:
            message = "Please provide a valid room ID."
        return render(request, 'delete_room.html', {'message': message})
    return render(request, 'delete_room.html')


def bookroom(request):
    if request.method == "POST":
        room_id = request.POST.get('room_id')
        if room_id:
            try:
                room = Room.objects.get(room_id=room_id)
                if room.status != 'Booked':  # Check if the room is already booked
                    room.status = 'Booked'
                    room.save()
                    message = f"Room {room_id} successfully booked."
                else:
                    message = "Room is already booked."
            except Room.DoesNotExist:
                message = f"Room {room_id} not found."
        else:
            message = "Please provide a valid room ID."
        return render(request, 'avaiblerooms.html', {'message': message})
    return render(request, 'bookroom.html')


def cancelbooking(request):
    if request.method == "POST":
        room_id = request.POST.get('room_id')
        if room_id:
            try:
                room = Room.objects.get(room_id=room_id)
                if room.status == 'Booked':  # Check if the room is booked
                    room.status = 'Available'
                    room.save()
                    message = f"Booking for room {room_id} has been cancelled."
                else:
                    message = "Room is not booked."
            except Room.DoesNotExist:
                message = f"Room {room_id} not found."
        else:
            message = "Please provide a valid room ID."
        return render(request, 'cancelbooking.html', {'message': message})
    return render(request, 'cancelbooking.html')

def avaiblerooms(request):
    available_rooms = Room.objects.filter(status='Available')
    return render(request, 'avaiblerooms.html', {'rooms': available_rooms})
