from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .Serilizers import *
from rest_framework import status
from rest_framework.response import Response
# Create your views here.



class Account_create(APIView):
    def get(self,request):
        try:
            account = Account.objects.all()
            serializer = AccountSerializer(account,many = True)
            return Response(serializer.data,status=status.HTTP_200_OK) 

        except Account.DoesNotExist:
            return Response({"error":"No data is here"},status=status.HTTP_403_FORBIDDEN) 

    def post(self,request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)        





class Account_creates(APIView):
    def get(self,request,pk):
        print("==============================================")
        try:
            account = Account.objects.get(id=pk)
            serializer = AccountSerializer(account)
            return Response(serializer.data,status=status.HTTP_200_OK) 

        except Account.DoesNotExist:
            return Response({"error":"No data is here"},status=status.HTTP_403_FORBIDDEN) 

    def put(self,request,pk):
            product = Account.objects.get(pk=pk)
            serializer = AccountSerializer(product,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

    def delete(self,request,pk):
        product = Account.objects.filter(id = pk).delete()
    
        return Response(status=status.HTTP_200_OK)
