from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def home(request):
    a={
        '1':"hjdsf",
        '2':"hjdsf",
        '3':"hjdsf",
        '4':"hjdsf",
        '5':"hjdsf",
    }
    return Response(a)

@api_view(['GET'])
def userList(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)