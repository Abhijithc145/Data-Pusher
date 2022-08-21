from telnetlib import SE
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .Serializer import *
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


# importing the requests library
import requests


class destinations(APIView):
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

class Get_destination(APIView):
    def get(request,self,pk):
        user = Dstinations.objects.get(Account_name__Account_id = pk)
        serializer = DestinationSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Incomingdata(APIView):
    def get(self,request):
        
        return Response({"error":"Invalid Data" })



    def post(self,request):
        user = request.headers.get('Secret-token')   
        if user == None:
             
            return Response({"error":"Unauthenticate"})
        else:
            if type(request.data)!=dict:
                return Response({"error":"Invalid Data" })
            else:
                if Account.objects.filter(Secret_token = user).exists():
                    Accounts = Account.objects.get(Secret_token = user)
                    for i  in Dstinations.objects.filter(Account_name = Accounts):
                        if i.Http_method == "GET":
                            try:
                                r = requests.get(url = i.Destination_Url, params = request.data)
                            except:
                                pass    
                              
                        elif i.Http_method == "POST":
                            try:
                                r = requests.post(url = i.Destination_Url, data=request.data, headers=i.Header)
                            except:
                                pass    

                        elif i.Http_method == "PUT":
                            try:
                                r = requests.put(url = i.Destination_Url, data=request.data, headers=i.Header)
                            except:
                                pass   

                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)    
        

        
             