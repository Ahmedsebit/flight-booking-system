from rest_framework import generics
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Q
import datetime
from bookings.models import Booking
from flight.models import Flight

from .serializers import BookingModelSerializer

from rest_framework.authtoken.models import Token


class BookingApiCustomerListView(generics.ListAPIView):
    '''
    Get all booking for a logged in user.
    '''

    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = BookingModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Booking.objects.filter(user__id=self.request.user.id)
        query = self.request.GET.get("q", None)
        query_day =  self.request.GET.get("day", None)
        print(query_day)
        if query_day is not None:
            qs = qs.filter(
                Q(ref__icontains=query)
                )
        return qs


class BookingApiListView(generics.ListAPIView):
    '''
    Get all bookings made. The request user needs to be admin
    '''
    permission_classes = [permissions.IsAdminUser]
    serializer_class = BookingModelSerializer
    
    
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q", None)
        query_day =  self.request.GET.get("day", None)
        print(query_day)

        qs = Booking.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(ref__icontains=query)
                )
        if query_day is not None:
            day = query_day.split(',')
            day = datetime.datetime(int(day[0]), int(day[1]), int(day[2]))
            print(day)
            qs = qs.filter(
                Q(timestamp__year=day.year, timestamp__month=day.month, timestamp__day=day.day)
                )
        return qs


class BookingAPICreateView(generics.CreateAPIView):
    '''
    Create a new booking
    '''
    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class BookingApiDetailView(generics.RetrieveAPIView):
    '''
    Get a booking details
    '''
    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class BookingApiDestroyView(generics.DestroyAPIView):
    '''
    Delete a booking
    '''
    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class BookingApiUpdateView(generics.UpdateAPIView):
    '''
    Update a booking
    '''
    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
