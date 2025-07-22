from rest_framework.serializers import *
from accounts.serializers.user_serializer import UserSerializer
from accounts.models.students import Student
class StudentSerializer(ModelSerializer):
    user=UserSerializer()
    class Meta:
        fields=['user','student_id']
        model= Student