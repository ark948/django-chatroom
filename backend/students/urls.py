from django.urls import path


# local imports
from students import views


app_name = "students"

urlpatterns = [
    path('new/', views.upload_file_view, name='new_file'),
    path('list/', views.view_user_files, name='list'),
    path('item/<int:item_id>', views.view_file, name='item'),
]