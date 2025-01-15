from django.urls import path, include



# local imports
from blog.views import add_post_view



app_name = 'blog'

urlpatterns = [
    path('add/', add_post_view, name='add')
]