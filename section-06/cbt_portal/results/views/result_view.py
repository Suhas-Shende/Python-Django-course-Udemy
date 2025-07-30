from rest_framework.viewsets import ModelViewSet
from results.serializers.result_serializer import ResultSerializer
from results.models.result import Result

class ResultViewset(ModelViewSet):
    queryset=Result.objects.all()
    serializer_class=ResultSerializer