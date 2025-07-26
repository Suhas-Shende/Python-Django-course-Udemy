from rest_framework.viewsets import ModelViewSet
from accounts.models.admin import Admin
from accounts.serializers.admin_serializer import AdminSerializer
# from rest_framework.permissions import AllowAny


class AdmintViewSet(ModelViewSet):
    # permission_classes=[AllowAny]    
    queryset=Admin.objects.all()
    serializer_class=AdminSerializer
    http_method_names=['get','put','patch','delete']

    