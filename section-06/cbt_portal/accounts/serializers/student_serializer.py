from rest_framework.serializers import *
from accounts.models.students import Student
class StudentSerializer(ModelSerializer):

    class Meta:
        fields=['user','student_id']
        model= Student