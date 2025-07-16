from django.urls import path
from courses.views.course_views import course_list
urlpatterns=[

    path("all",course_list,name="listallcourses")
]