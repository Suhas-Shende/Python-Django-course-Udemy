from rest_framework.serializers import ModelSerializer
from questions.models.exam_choice import ExamChoice

class ExamChoiceSerializer(ModelSerializer):
    class Meta:
        fields=['question','choice_text']
        model= ExamChoice
        depth=3