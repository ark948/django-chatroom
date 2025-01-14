from django.urls import path


from accounts.views import (
    signup_view,
    login_view,
    logout_view,
    profile
)

app_name="accounts"

urlpatterns = [
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile')
]