from rest_framework.viewsets import ModelViewSet
from accounts.models.students import Student
from accounts.serializers.student_serializer import StudentSerializer
from accounts.permissions.isStudentOrReadOnly import IsStudentOrAdminReadOnly
class StudentViewSet(ModelViewSet):
    permission_classes=[IsStudentOrAdminReadOnly]        
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    http_method_names=['get','put','patch','delete']