from django.urls import path


from accounts_api import views


app_name='accounts_api'

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='api_register'),
    path('login/', views.UserLoginAPIView.as_view(), name='api_login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='api_logout'),
]