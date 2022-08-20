from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .Serializer import *
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class Incomingdata(APIView):
        def get(self,request):
            try:
                account = Dstinations.objects.all()
                serializer = DestinationSerializer(account,many = True)
                return Response(serializer.data,status=status.HTTP_200_OK) 

            except Dstinations.DoesNotExist:
                return Response({"error":"No data is here"},status=status.HTTP_403_FORBIDDEN) 

        def post(self,request):
            serializer = DestinationSerializer(data=request.data)
            if serializer.is_valid():
                
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors)        
