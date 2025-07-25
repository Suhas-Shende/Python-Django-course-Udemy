
from rest_framework.serializers import *
from accounts.models.admin import Admin
class AdminSerializer(ModelSerializer):
   
    class Meta:
        fields=['user','department']
        model=Admin
        