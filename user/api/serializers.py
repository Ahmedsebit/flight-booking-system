from django.contrib.auth import get_user_model
from django.utils.timesince import timesince
from rest_framework import serializers
from django.urls import reverse_lazy
from user.models import CustomUser

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            'name',
            'birth_date',
            'nationality',
            'country_of_residence',
            'travel_document_type',
            'travel_document_number',
            'phone',
            'address',
            'gender'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email', 'username', 'name', 'birth_date', 'nationality', 'country_of_residence', 'travel_document_type', 'travel_document_number', 'phone', 'address', 'gender')

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'birth_date', 'nationality', 'country_of_residence', 'travel_document_type', 'travel_document_number', 'phone', 'address', 'gender')