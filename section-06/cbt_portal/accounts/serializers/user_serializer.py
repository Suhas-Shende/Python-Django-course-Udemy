from rest_framework.serializers import *
from accounts.models.user import CBTCustomUser
from accounts.models.admin import Admin
from accounts.models.students import Student
class UserSerializer(ModelSerializer):
    password=CharField(write_only=True)
    role=ChoiceField(choices=['student','admin'],write_only=True)
    student_id=CharField(required=False,allow_blank=True)
    department=CharField(required=False)
    class Meta:
        fields=['first_name','last_name','email','username','password','role','student_id','department']
        model=CBTCustomUser

    def create(self, validated_data):
        # Seperate the data
        role=validated_data.pop('role')
        student_id=validated_data.pop('student_id',None)
        department=validated_data.pop('department',None)
        password=validated_data.pop('password')
        
        # Creating a cbt user account/instance

        user=CBTCustomUser(**validated_data)
        user.is_admin=role=='admin'
        user.is_student=role=='student'
        user.set_password(password)
        user.save()


        if role=='admin':
            Admin.objects.create(user=user,department=department)
        elif role=='student':
             Student.objects.create(user=user,student_id=student_id)
        return user