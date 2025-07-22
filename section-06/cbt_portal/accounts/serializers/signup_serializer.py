from rest_framework.serializers import *


class SignupSerializer(Serializer):
    username=CharField()
    email=CharField()
    role=CharField()
    password=CharField()