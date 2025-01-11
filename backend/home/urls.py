from django.urls import path


# local imports
from home.views import index


app_name = "home"

urlpatterns = [
    path('', index, name='index')
]