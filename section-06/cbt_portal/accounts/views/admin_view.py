from rest_framework.viewsets import ModelViewSet
from accounts.models.admin import Admin
from accounts.serializers.admin_serializer import AdminSerializer

class AdmintViewSet(ModelViewSet):
    queryset=Admin.objects.all()
    serializer_class=AdminSerializer

    