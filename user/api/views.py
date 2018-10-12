from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User

from .serializers import UserDisplaySerializer, UserSerializer, UserUpdateSerializer

from user.models import CustomUser


class UserApiCreateView(generics.CreateAPIView):
    serializer_class = UserDisplaySerializer
    

class UserApiListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserApiDetailListView(generics.ListAPIView):
    # queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self, *args, **kwargs):
        qs = CustomUser.objects.filter(id=self.request.user.id)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(username__icontains=query) 
                )
        return qs

class CustomUserApiDetailView(generics.RetrieveAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JSONWebTokenAuthentication, )


class CustomUserApiDestroyView(generics.DestroyAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomUserApiUpdateView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]