
from rest_framework.serializers import *
from accounts.serializers.user_serializer import UserSerializer
from accounts.models.admin import Admin
class AdminSerializer(ModelSerializer):
    user=UserSerializer()
    class Meta:
        fields=['user','department']
        model=Admin
        