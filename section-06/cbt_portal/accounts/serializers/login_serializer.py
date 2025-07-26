from rest_framework.serializers import *
from django.contrib.auth import authenticate

class LoginSerializer(Serializer):
    username=CharField()
    password=CharField(write_only=True)
    def validate(self,data):
        user=authenticate(username=data['username'],password=data['password'])
        if not user:
           raise ValidationError('username or password or both are invalid')
        if not user.is_active:
            raise ValidationError('user is not active')
        data['user']=user
        return data
    

    # {
    #    'username':'suhas',
    #    'password':'13421',
    #    'user': {
    #               'username':'suhas',
    #               'password':'13421',
    #    }

    # }