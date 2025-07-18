from django.db.models import *
from courses.models.exam import Exam

class ExamQuestion(Model):
    exam=OneToOneField(Exam,on_delete=CASCADE)
    quetion_text=CharField(max_length=200)
    marks=IntegerField()
    def __str__(self):
        return f'{self.quetion_text}'


    