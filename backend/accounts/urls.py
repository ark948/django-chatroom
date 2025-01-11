from django.urls import path


from accounts.views import (
    CustomRegisterView,
    CustomLoginView,
    signup_view,
    login_view,
    logout_view
)

# app_name="accounts" not doing this

urlpatterns = [
    path("signup/", CustomRegisterView.as_view(), name="accounts_signup"),
    path("login/", CustomLoginView.as_view(), name="accounts_login"),
    path('signup-v2/', signup_view, name="signup_v2"),
    path('login-v2/', login_view, name="login_v2"),
    path('logout/', logout_view, name='logout')
]