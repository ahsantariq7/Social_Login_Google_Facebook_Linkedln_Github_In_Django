from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User
#from .serializers import Custom_Login

# Create your views here.
def callback(request):
    return render(request,'ahsan.html')

#class Users_View(ListCreateAPIView):
  #  queryset=User
  #  serializer_class=Custom_Login

