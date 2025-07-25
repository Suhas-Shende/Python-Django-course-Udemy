from rest_framework.viewsets import ModelViewSet
from accounts.models.students import Student
from accounts.serializers.student_serializer import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    