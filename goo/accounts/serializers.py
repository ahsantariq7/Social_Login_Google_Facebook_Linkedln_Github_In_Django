from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomLoginSerializer(LoginSerializer):
    username = None


class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    genre = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    marital_status = serializers.CharField(required=False, allow_blank=True)
    number_of_children = serializers.IntegerField(required=False)
    socio_professional_category = serializers.CharField(required=False, allow_blank=True)
    annual_income = serializers.FloatField(required=False)
    annual_net_income_after_charges = serializers.FloatField(required=False)
    amount_to_deposit_in_the_robot = serializers.FloatField(required=False)
    country_of_residence = serializers.CharField(required=False, allow_blank=True)
    address_of_residence = serializers.CharField(required=False, allow_blank=True)
    agree_to_contact_back = serializers.BooleanField(required=True)
    agree_to_terms_and_conditions = serializers.BooleanField(required=True)

    