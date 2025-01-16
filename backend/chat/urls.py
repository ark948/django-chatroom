from django.urls import path, include



from chat import views


urlpatterns = [
    path("", views.chat_page_view, name="chat-page"),
]