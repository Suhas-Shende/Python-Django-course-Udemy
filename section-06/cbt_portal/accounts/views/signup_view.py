from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from accounts.serializers.user_serializer import UserSerializer
from rest_framework.permissions import AllowAny
class SignupView(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,HTTP_201_CREATED)
        return Response(serializer.errors,HTTP_400_BAD_REQUEST)

    
{
      
          "email":"Suhas@123.gcom",
         "username":"Pratik",
         "password":"1234",
         "first_name":"Sharvari",
         "last_name":"Wagh"

        }