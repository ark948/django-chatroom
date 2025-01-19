from django.urls import path


# local imports
from home import views


app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
]