from rest_framework import generics
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Q
from bookings.models import Booking

from .serializers import BookingModelSerializer

from rest_framework.authtoken.models import Token


class BookingApiCustomerListView(generics.ListAPIView):

    authentication_classes = (JSONWebTokenAuthentication)
    serializer_class = BookingModelSerializer

    def get_queryset(self, *args, **kwargs):

        qs = Booking.objects.filter(user__user=self.request.user)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(ref__icontains=query)
                )
        return qs


class BookingApiListView(generics.ListAPIView):

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
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingApiDetailView(generics.RetrieveAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingApiDestroyView(generics.DestroyAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookingApiUpdateView(generics.UpdateAPIView):

    queryset = Booking.objects.all()
    serializer_class = BookingModelSerializer
    permission_classes = [permissions.IsAuthenticated]
