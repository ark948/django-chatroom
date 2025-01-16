from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.



def chat_page_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))
    context = {}
    return render(request, 'chat/chat_page.html', context)