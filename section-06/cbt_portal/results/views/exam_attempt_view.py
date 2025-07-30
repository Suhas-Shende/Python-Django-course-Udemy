from rest_framework.viewsets import ModelViewSet
from results.serializers.exam_attemp_serializer import ExamAttemptSerializer
from results.models.exam_attempt import ExamAttempt

class ExamAttemptViewset(ModelViewSet):
    queryset=ExamAttempt.objects.all()
    serializer_class=ExamAttemptSerializer