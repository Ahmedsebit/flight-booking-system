from django.shortcuts import render

from django.urls import reverse_lazy, reverse

# Create your views here.
from django.views.generic.edit import CreateView
from .forms import BookingModelForm
from flight.models import Flight
from customer_account.models import CustomerAccount
from seats.models import Seat
from bookings.models import Booking

class BookingCreateView(CreateView):
    form_class  = BookingModelForm
    template_name = 'bookings_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        flight = Flight.objects.get(id=self.kwargs['pk'])
        context['flight'] = flight
        context['user'] = CustomerAccount.objects.get(id=self.request.user.id)
        context['booked_seats'] = bookings = Booking.objects.filter(flight__id=flight.id)
        context['seats'] = Seat.objects.all()
        success_url = reverse_lazy("index") 
        return context