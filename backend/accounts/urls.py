from django.urls import path


from accounts.views import (
    CustomRegisterView,
    CustomLoginView,
    logout_view,
    profile
)

app_name="accounts"

urlpatterns = [
    path('signup/', CustomRegisterView.as_view(), name="signup"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile')
]