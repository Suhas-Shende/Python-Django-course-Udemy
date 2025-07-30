from rest_framework.routers import SimpleRouter
from .views.exam_attempt_view import ExamAttemptViewset
from results.views.result_view import ResultViewset
from results.views.student_answer_view import StudentAnswerViewset

from django.urls import path,include

router=SimpleRouter()
router.register('exam-attempt',ExamAttemptViewset)
router.register('student-answer',StudentAnswerViewset)
router.register('',ResultViewset)


urlpatterns=[
    path('',include(router.urls))
    
]