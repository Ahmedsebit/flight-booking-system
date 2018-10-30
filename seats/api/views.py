from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import SeatModelSerializer

from seats.models import Seat


class SeatApiCreateView(generics.CreateAPIView):
    '''
    Create a seat. The request user needs to be admin
    '''
    serializer_class = SeatModelSerializer
    permission_classes = [permissions.IsAdminUser]

class SeatApiListView(generics.ListAPIView):
    '''
    List all seats.
    '''
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
    '''
    Get  a seat detail.
    '''
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    permission_classes = [permissions.IsAdminUser]


class SeatApiDestroyView(generics.DestroyAPIView):
    '''
    Delete a seat
    '''
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    permission_classes = [permissions.IsAdminUser]


class SeatApiUpdateView(generics.UpdateAPIView):
    '''
    Update a seat
    '''
    queryset = Seat.objects.all()
    serializer_class = SeatModelSerializer
    permission_classes = [permissions.IsAdminUser]