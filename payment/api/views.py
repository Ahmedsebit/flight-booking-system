from rest_framework import generics
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Q
from payment.models import Payment

from .serializers import PaymentModelSerializer

from rest_framework.authtoken.models import Token


class PaymentApiCustomerListView(generics.ListAPIView):
    '''
    Get a logged in users all payments 
    '''
    authentication_classes = (JSONWebTokenAuthentication, )
    serializer_class = PaymentModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Payment.objects.filter(booking__user__id=self.request.user.id)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(ref__icontains=query)
                )
        return qs


class PaymentApiListView(generics.ListAPIView):

    '''
    Get all payments. The request user needs to be admin
    '''
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PaymentModelSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = Payment.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(ref__icontains=query)
                )
        return qs


class PaymentAPICreateView(generics.CreateAPIView):
    '''
    Create a new payment
    '''
    serializer_class = PaymentModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class PaymentApiDetailView(generics.RetrieveAPIView):

    '''
    Update a payment
    '''
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
    authentication_classes = (JSONWebTokenAuthentication, )


class PaymentApiDestroyView(generics.DestroyAPIView):
    '''
    Delete a payment. The request user needs to be admin
    '''
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
    permission_classes = [permissions.IsAdminUser]


class PaymentApiUpdateView(generics.UpdateAPIView):
    '''
    Update a payment
    '''
    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer
    permission_classes = [permissions.IsAdminUser]
