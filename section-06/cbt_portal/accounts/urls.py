from  rest_framework.routers import SimpleRouter
from accounts.views.student_view import StudentViewSet
from accounts.views.signup_view import SignupView
from accounts.views.admin_view import AdmintViewSet
from django.urls import path
from accounts.views.login_view import *

app_name='accounts'
router=SimpleRouter()
router.register(r'students',StudentViewSet)
router.register(r'admin',AdmintViewSet)

urlpatterns=[

    path('signup/',SignupView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]
urlpatterns +=router.urls

