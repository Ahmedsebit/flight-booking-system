from rest_framework import serializers
from user.api.serializers import UserDisplaySerializer
from rest_framework.fields import CurrentUserDefault

from customer_account.models import CustomerAccount

class CustomerAccountModelSerializer(serializers.ModelSerializer):

    # user = UserDisplaySerializer(read_only=True)

    class Meta:
        model = CustomerAccount
        fields = [
            # 'user',
            "bio",
            'birth_date',
            "country_of_residence",
            "travel_document_type",
            "travel_document_number",
            "phone",
            "address",
            "gender",
        ]

    def save(self):
        user = CurrentUserDefault()