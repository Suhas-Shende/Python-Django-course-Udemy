from django.urls import path
from poll.views import *
urlpatterns=[
path('first/',index),
path('<int:question_id>/',detail,name="grab_questions"),

path('<int:question_id>/results',results,name="results"),
path('<int:question_id>/vote',vote,name="results")
]