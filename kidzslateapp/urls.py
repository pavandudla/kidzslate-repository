# from django.contrib import admin
# from django.urls import path
# from .views import *
# from rest_framework.authtoken import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("get/", Readstudent),
#     path('student_register/', RegisterView.as_view(), name='register'),
#     path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('add_student_data/', AuthView.as_view(), name='add_student'),
#
#     # path('register/', RegisterView.as_view(), name='register'),
# ]





from django.contrib import admin
from django.urls import path
# from .views import Readstudent, RegisterView, CustomTokenObtainPairView, AuthView, ProtectedView

from .views import LoginApi,Readstudent,Addstudentdata,register, profile
# from .views import request_password_reset, password_reset_confirm        ,ProtectedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("get/", Readstudent),
    path("add/", Addstudentdata),
    # path('student_register/', RegisterView.as_view(), name='register'),
    # path('login/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('add_student_data/', AuthView.as_view(), name='add_student'),
    # path('protected/', ProtectedView.as_view(), name='protected_view'),
    path('register/', register, name='register'),
    path('loginApi/', LoginApi.as_view(), name='login'),
    path('profile/', profile, name='profile'),

    # path('request-password-reset/', request_password_reset, name='request_password_reset'),
    # path('password-reset-confirm/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
]
