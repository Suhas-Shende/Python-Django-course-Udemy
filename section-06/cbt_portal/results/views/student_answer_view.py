from rest_framework.viewsets import ModelViewSet
from results.serializers.student_answer_serializer import StudentAnswerSerializer
from results.models.student_answer import StudentAnswer

class StudentAnswerViewset(ModelViewSet):
    queryset=StudentAnswer.objects.all()
    serializer_class=StudentAnswerSerializer