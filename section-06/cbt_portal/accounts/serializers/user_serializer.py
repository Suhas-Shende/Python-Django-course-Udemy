from rest_framework.serializers import *
from accounts.models.user import CBTCustomUser
class UserSerializer(ModelSerializer):
    password=CharField(write_only=True)
    class Meta:
        fields=['first_name','last_name','email','username','password']
        model=CBTCustomUser

