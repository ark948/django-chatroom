from django.urls import path, include



# local imports
from blog.views import add_post_view, add_post_view_v2
from blog import views



app_name = 'blog'

urlpatterns = [
    path('add/', add_post_view, name='add'),
    path('add2/', add_post_view_v2, name='add2'),
    path('add3/', views.add_post_view_v3, name='add3'),
    path('add4/', views.add_post_view_v4, name='add4')
]