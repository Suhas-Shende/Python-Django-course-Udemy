from django.urls import path
from courses.views.course_views import *
from courses.views.exam_views import *

app_name="courses"
urlpatterns=[

   # Course Pattern as APIView based class
#    path("all",CourseListView.as_view(),name="listallcourses"),
#    path("<int:pk>",CourseDetailUpdateDeleteView.as_view(),name="onecoursedetail"),

       #OR

   #Course View based on @apiview decorators
    # path("all",course_list,name="listallcourses"),
    # path("<int:pk>",course_detail,name="onecoursedetail")

     #OR
    #Course View based on APIViewset
   path("all",CourseViewSet.as_view({'get':'list'}),name="listallcourses"),
   path("<int:pk>",CourseViewSet.as_view({'get':'retrieve'}),name="onecoursedetail"),
    




    # Exam Pattern
    path("exams/all",ExamCreateListView.as_view(),name="exam-list"),
    path("exams/<slug:pk>",ExamDetailUpdateDeleteView.as_view(),name="exam-detail"),
]