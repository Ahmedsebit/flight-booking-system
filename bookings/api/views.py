from rest_framework import generics
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Q
from bookings.models import Booking
from flight.models import Flight

from .serializers import BookingModelSerializer

from rest_framework.authtoken.models import Token


class BookingApiCustomerListView(generics.ListAPIView):

    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = BookingModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Booking.objects.filter(user__id=self.request.user.id)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(ref__icontains=query)
                )
        return qs


class BookingApiListView(generics.ListAPIView):

    permission_classes = [permissions.IsAdminUser]
    serializer_class = BookingModelSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = Booking.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(ref__icontains=query)
                )
        return qs


class BookingAPICreateView(generics.CreateAPIView):

    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class BookingApiDetailView(generics.RetrieveAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class BookingApiDestroyView(generics.DestroyAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class BookingApiUpdateView(generics.UpdateAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
