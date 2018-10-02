from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q
from flight.models import Flight

from .serializers import FlightModelSerializer

class FlightApiListView(generics.ListAPIView):

    serializer_class = FlightModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Flight.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query) 
                )
        return qs


class FlightAPICreateView(generics.CreateAPIView):

    serializer_class = FlightModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)