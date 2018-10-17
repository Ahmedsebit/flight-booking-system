from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import SeatModelSerializer

from seats.models import Seat


class SeatApiCreateView(generics.CreateAPIView):
    serializer_class = SeatModelSerializer

class SeatApiListView(generics.ListAPIView):
    serializer_class = SeatModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )

    authentication_classes = (JSONWebTokenAuthentication, )
    def get_queryset(self, *args, **kwargs):
        qs = Seat.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(username__icontains=query) 
                )
        return qs

class SeatApiDetailView(generics.RetrieveAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class SeatApiDestroyView(generics.DestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class SeatApiUpdateView(generics.UpdateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )