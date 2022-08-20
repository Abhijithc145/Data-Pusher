from rest_framework import serializers
from .models import *



class DriverRegistrationfirstSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    def create(self,validated_data):
        user = Account.objects.create(
            username = validated_data['username'],
            phone_number =validated_data['phone_number'],
            is_staff = True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user