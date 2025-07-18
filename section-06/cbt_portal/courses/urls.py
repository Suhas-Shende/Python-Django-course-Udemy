from django.urls import path
from courses.views.course_views import *
from courses.views.exam_views import *

app_name="courses"
urlpatterns=[

   # Course Pattern
    # path("all",course_list,name="listallcourses"),
    path("all",CourseListView.as_view(),name="listallcourses"),
    # path("<int:pk>",course_detail,name="onecoursedetail")
    path("<int:pk>",CourseDetailUpdateDeleteView.as_view(),name="onecoursedetail"),

    # Exam Pattern
    path("exams/all",ExamCreateListView.as_view(),name="exam-list"),
    path("exams/<slug:pk>",ExamDetailUpdateDeleteView.as_view(),name="exam-detail"),
]