from rest_framework.serializers import *
from django.contrib.auth import authenticate

class LoginSerializer(Serializer):
    username=CharField
    password=CharField(write_only=True)
    def validate(self,data):
        user=authenticate(data['username'],data['password'])
        if user:
            return 'Login successfully'
        else:
            return 'username or password or both are invalid'