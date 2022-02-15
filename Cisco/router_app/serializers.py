from rest_framework import serializers
from .models import router_detail
from django.contrib.auth.models import User

class router_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model=router_detail
        fields=('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','first_name','last_name']
    

