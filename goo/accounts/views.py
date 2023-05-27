from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer,CustomRegisterSerializer
from dj_rest_auth.registration.views import RegisterView
from django.shortcuts import HttpResponse
from django.contrib.auth import get_user_model
from django.shortcuts import render
import requests


User = get_user_model()



class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer


class CustomRegisterView(RegisterView):
    serializer_class=CustomRegisterSerializer


def my_view(request):
    response = requests.get('http://127.0.0.1:8000/model/textapi/')
    data = response.json()
    return HttpResponse(data)

