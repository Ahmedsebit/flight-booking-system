from django.shortcuts import render
from django.shortcuts import get_object_or_404
from flight.models import Flight
from seats.models import Seat
from bookings.models import Booking
from customer_account.models import CustomerAccount

def home(request):
    return render(request, "home.html", {})

def index(request):
    return render(request, "index.html", {})

def book(request, pk, id):
    flight = Flight.objects.get(id=pk)
    seats = Seat.objects.all()
    bookings = Booking.objects.filter(flight__id=flight.id)
    user = CustomerAccount.objects.get(id=id)
    booked_seats = []
    for booking in bookings:
        booked_seats.append(booking.seat)
    context = {'user':user,'flight': flight,'seats':seats,'booked_seats':booked_seats}
    return render(request, "book.html", context)