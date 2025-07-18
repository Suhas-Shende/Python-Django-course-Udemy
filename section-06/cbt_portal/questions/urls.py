from django.urls import path,include
from .views.exam_choice_view import *
app_name='questions'
urlpatterns = [

    path("choices/all/",ExamChoiceView.as_view(),name="exam-choices-list"),
    path('choices/<int:pk>/',ExamChoiceDetailUpdateDeleteView.as_view(),name="exam-choice-detail")


]
