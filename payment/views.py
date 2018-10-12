from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from .forms import PaymentModelForm
from bookings.models import Booking

class PaymentCreateView(CreateView):
    form_class  = PaymentModelForm
    template_name = 'payment_form.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        booking = Booking.objects.get(ref=self.kwargs['pk'])
        context['booking'] = booking
        return context