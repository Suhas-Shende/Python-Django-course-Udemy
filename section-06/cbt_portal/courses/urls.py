from django.urls import path
from courses.views.course_views import *
urlpatterns=[

    # path("all",course_list,name="listallcourses"),
    path("all",CourseListView.as_view(),name="listallcourses"),
    # path("<int:pk>",course_detail,name="onecoursedetail")
    path("<int:pk>",CourseDetailUpdateDelete.as_view(),name="onecoursedetail")
]