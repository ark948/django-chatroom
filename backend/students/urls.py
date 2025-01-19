from django.urls import path


# local imports
from students import views


app_name = "students"

urlpatterns = [
    path('new/', views.upload_file_view, name='new_file'),
]