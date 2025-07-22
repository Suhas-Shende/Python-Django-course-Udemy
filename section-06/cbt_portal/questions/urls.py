from django.urls import path,include
from .views.exam_choice_view import *
from .views.exam_question_view import *
app_name='questions'
urlpatterns = [
   #Exam Questions Patterns
    path("all/",ExamQuestionView.as_view(),name="exam-question-list"),
    path('<int:pk>/',ExamQuestionDetailUpdateDeleteView.as_view(),name="exam-question-detail"),




    #Exam Questions Choices Patterns
    path("choices/all/<int:pk>",ExamChoiceView.as_view(),name="exam-choices-list"),
    path('choices/<int:pk>/',ExamChoiceDetailUpdateDeleteView.as_view(),name="exam-choice-detail")


]
