from django.db.models import *
from accounts.models.students import Student
from questions.models.exam_choice import ExamChoice
from questions.models.exam_question import ExamQuestion
from results.models.exam_attempt import ExamAttempt

class StudentAnswer(Model):
    student=ForeignKey(Student,on_delete=CASCADE,related_name="student_answer")
    question= ForeignKey(ExamQuestion,on_delete=Case,related_name="exam_attempts")
    selected_choice=ForeignKey(ExamChoice,on_delete=CASCADE)
    attempt=ForeignKey(ExamAttempt,on_delete=CASCADE)
    

    def __str__(self):
        return "This is the %s answer to % attempted by %s" %\
           (self.selected_choice,self.question.question_text,self.student.username)
    
