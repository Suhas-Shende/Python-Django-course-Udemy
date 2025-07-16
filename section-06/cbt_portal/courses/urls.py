from django.urls import path
from courses.views.course_views import *
urlpatterns=[

    path("all",course_list,name="listallcourses"),
    path("<int:pk>",course_detail,name="onecoursedetail")
]