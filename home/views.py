from django.shortcuts import render, get_object_or_404, redirect
from home.models import Room

def index(request):
    return render(request, 'index.html')

# To view all the rooms
def view_all_rooms(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        return render(request, 'view_all_rooms.html', {'rooms': rooms})

# For the admin to add a room
def addroom(request):
    if request.method == "POST":
        roomid = request.POST.get('roomid')
        status = request.POST.get('status')
        if roomid and status:
            room = Room(room_id=roomid, status=status)
            room.save()
            message = "Room successfully added"
        else:
            message = "Provide all the necessary details"
        return render(request, 'addroom.html', {'message': message})
    return render(request, 'addroom.html')

# To update the room status
def update_room(request):
    if request.method == "POST":
        room_id = request.POST.get('roomid')  
        new_status = request.POST.get('status')
        if room_id and new_status:
            try:
                room = Room.objects.get(room_id=room_id)
                room.status = new_status
                room.save()
                message = f"Room {room_id} status updated successfully to '{new_status}'."
            except Room.DoesNotExist:
                message = f"No room found with ID {room_id}."
        else:
            message = "Please provide both Room ID and Status."
        return render(request, 'update_room.html', {'message': message})
    return render(request, 'update_room.html')


# to delete a room 
def delete_room(request):
    if request.method == "POST":
        room_id = request.POST.get('roomid')
        if room_id:
                room = Room.objects.get(room_id=room_id)
                room.delete()
        return redirect('viewallrooms')
    return render(request, 'delete_room.html')
