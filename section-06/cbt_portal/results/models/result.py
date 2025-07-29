from django.db.models import *
from accounts.models.students import Student
from courses.models.exam import Exam

class Result(Model):
    student=ForeignKey(Student,on_delete=CASCADE,related_name="exam_attempts")
    exam= ForeignKey(Exam,on_delete=Case,related_name="exam_attempts")
    score=IntegerField(default=0)