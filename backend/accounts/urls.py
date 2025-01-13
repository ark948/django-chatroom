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
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout')
]