# Hotel Room Booking System

This is a Django-based project that provides a Hotel Room Booking System. The project includes secure CRUD operations, user-friendly code, and protected routes. The database operations are managed using the Django Admin panel.

## Features

### Admin Endpoints
1. View All Rooms
   - Endpoint: `GET /admin/rooms`
   - Description: Retrieve a list of all rooms in the hotel.

2. Add a New Room
   - Endpoint: `POST /admin/rooms`
   - Description: Add a new room to the hotel's inventory.

3. Update Room Details
   - Endpoint: `PUT /admin/rooms/<room_id>`
   - Description: Update the details of an existing room using its unique ID.

4. Delete a Room
   - Endpoint: `DELETE /admin/rooms/<room_id>`
   - Description: Remove a room from the hotel's inventory using its unique ID.

### User Endpoints
1. Search Available Rooms
   - Endpoint: `GET /rooms`
   - Description: Search and view available rooms for booking.

2. Book a Room
   - Endpoint: `POST /rooms/book`
   - Description: Book a room by providing the necessary details.

3. Cancel Booking
   - Endpoint: `DELETE /rooms/cancel`
   - Description: Cancel an existing booking.

## Prerequisites
1. Python (3.x)
2. Django Framework
3. Virtual Environment (recommended)

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/SamarthSahu366/hotel_room_mngmt
   cd hotel_room_mngmt
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for Django Admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Accessing the Application
- Admin Panel: Visit `http://127.0.0.1:8000/admin` to manage rooms and bookings (requires superuser credentials).
- User Endpoints: Utilize tools like Postman or cURL to interact with the user-facing APIs.

## Project Structure
```
project-directory/
|-- hotelManagement/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- rooms/
|   |-- migrations/
|   |-- admin.py
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|-- templates/
|-- static/
|-- manage.py
```

## Additional Notes
- Ensure proper authentication is set up for protected routes.
- This project is designed for learning purposes and can be further extended for production use.

Feel free to contribute or report issues!

