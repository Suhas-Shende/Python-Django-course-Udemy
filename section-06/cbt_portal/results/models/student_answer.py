from django.db.models import *
from accounts.models.students import Student
from questions.models.exam_choice import ExamChoice
from questions.models.exam_question import ExamQuestion
from results.models.exam_attempt import ExamAttempt

class StudentAnswer(Model):
    student=ForeignKey(Student,on_delete=CASCADE,related_name="student_answer")
    question= ForeignKey(ExamQuestion,on_delete=Case,related_name="student_answer")
    selected_choice=ForeignKey(ExamChoice,on_delete=CASCADE,related_name="student_answer")
    attempt=ForeignKey(ExamAttempt,on_delete=CASCADE,related_name="student_answer")
    

    def __str__(self):
        return "This is the %s answer to question: %s attempted by %s" %\
           (self.selected_choice,self.question.question_text,self.student.user.username)
    
