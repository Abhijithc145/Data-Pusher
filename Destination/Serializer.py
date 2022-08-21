from rest_framework import serializers
from .models import *
from Account.Serilizers import AccountSerializer


class DestinationSerializer(serializers.ModelSerializer):
    Account_name = AccountSerializer()
    class Meta:
        model =Dstinations

        fields = "__all__"

    