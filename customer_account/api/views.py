from rest_framework import generics
from django.db.models import Q
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from customer_account.models import CustomerAccount
from django.contrib.auth.models import User

from .serializers import CustomerAccountModelSerializer


class CustomerAccountApiListView(generics.ListAPIView):

    serializer_class = CustomerAccountModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )
    
    def get_queryset(self, *args, **kwargs):
        qs = CustomerAccount.objects.filter(user__id=self.request.user.id)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(user__username__icontains=query) 
                )
        return qs

class CustomerAccountApiCreateView(generics.CreateAPIView):

    serializer_class = CustomerAccountModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class CustomerAccountApiDetailView(generics.RetrieveAPIView):

    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (JSONWebTokenAuthentication, )


class CustomerAccountApiDestroyView(generics.DestroyAPIView):

    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountModelSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomerAccountApiUpdateView(generics.UpdateAPIView):

    queryset = CustomerAccount.objects.all()
    serializer_class = CustomerAccountModelSerializer
    permission_classes = [permissions.IsAuthenticated]