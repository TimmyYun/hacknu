from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from api.models import *


class SupplySerializer(ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'
