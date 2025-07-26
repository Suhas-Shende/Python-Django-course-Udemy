from rest_framework.viewsets import ModelViewSet
from accounts.models.students import Student
from accounts.serializers.student_serializer import StudentSerializer
from rest_framework.permissions import AllowAny
class StudentViewSet(ModelViewSet):
    permission_classes=[AllowAny]        
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    http_method_names=['get','put','patch','delete']