from rest_framework import generics
from django.db.models import Q
from customer_account.models import CustomerAccount

from .serializers import CustomerAccountModelSerializer

class CustomerAccountApiListView(generics.ListAPIView):

    serializer_class = CustomerAccountModelSerializer
    
    def get_queryset(self, *args, **kwargs):
        qs = CustomerAccount.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(user__username__icontains=query) 
                )
        return qs