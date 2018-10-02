from django.contrib.auth import get_user_model
from django.utils.timesince import timesince
from rest_framework import serializers
from django.urls import reverse_lazy

User = get_user_model()


class UserDisplaySerializer(serializers.ModelSerializer):

    
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name"
        ]
