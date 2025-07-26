from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.authtoken.models import Token
from accounts.models.students import Student
from accounts.models.admin import Admin
from accounts.serializers.login_serializer import LoginSerializer
from accounts.serializers.user_serializer import UserSerializer


class LoginView(APIView):
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            token,_=Token.objects.get_or_create(user=user)
            # role='student' if user.is_student else 'admin' if user.is_admin else 'user'
            return Response({
                'token':token.key,
                'user':UserSerializer(user).data,
             
            })
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        #Delete the token
        request.user.auth_token.delete()
        return Response(stutus=status.HTTP_204_NO_CONTENT)