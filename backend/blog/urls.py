from django.urls import path



# local imports
from blog import views



app_name = 'blog'
urlpatterns = [
    path('add/', views.add_post_view, name='new'),
    path('user-posts/', views.get_users_posts, name='users_list'),
    path('upload/', views.file_upload_view, name='file_upload'),
]