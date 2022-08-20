from rest_framework import serializers
from .models import *



class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model =Dstinations

        fields = "__all__"

    