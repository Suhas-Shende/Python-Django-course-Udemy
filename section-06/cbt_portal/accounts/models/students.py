from accounts.models.user import CBTCustomUser
from django.db.models import *


class Student(Model):
    user=OneToOneField(CBTCustomUser,on_delete=CASCADE)
    student_id=CharField(max_length=100)
    def __str__(self):
        return self.user.username
