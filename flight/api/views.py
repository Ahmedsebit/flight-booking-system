from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from flight.models import Flight
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import FlightModelSerializer, FlightModelUpdateSerializer


class FlightApiListView(generics.ListAPIView):

    serializer_class = FlightModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Flight.objects.all()
        location = self.request.GET.get("location", None)
        destination = self.request.GET.get("destination", None)
        date = self.request.GET.get("date", None)
        return_date = self.request.GET.get("return_date", None)
        
        if location is not None:
            qs = qs.filter(
                Q(location__icontains=location) 
                )
        if destination is not None:
            qs = qs.filter(
                Q(destination__icontains=destination) 
                )
        if date is not None:
            qs = qs.filter(
                Q(date__iexact=date) 
                )
        return qs


class FlightAPICreateView(generics.CreateAPIView):

    serializer_class = FlightModelSerializer
    permission_classes = [permissions.IsAdminUser]


class FlightApiDetailView(generics.RetrieveAPIView):

    queryset = Flight.objects.all()
    serializer_class = FlightModelSerializer


class FlightApiDestroyView(generics.DestroyAPIView):

    queryset = Flight.objects.all()
    serializer_class = FlightModelSerializer
    permission_classes = [permissions.IsAdminUser]


class FlightApiUpdateView(generics.UpdateAPIView):

    queryset = Flight.objects.all()
    serializer_class = FlightModelUpdateSerializer
    permission_classes = [permissions.IsAdminUser]