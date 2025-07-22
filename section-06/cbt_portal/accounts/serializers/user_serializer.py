from rest_framework.serializers import *
from accounts.models.user import CBTCustomUser
class UserSerializer(ModelSerializer):
    class Meta:
        fields=['id','first_name','last_name','email','username']
        model=CBTCustomUser