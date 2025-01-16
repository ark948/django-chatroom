from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView



# local imports
from blog import forms
from blog.models import Post





def add_post_view(request: HttpRequest):
    if request.method == "POST":
        form = forms.NewPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            body = form.cleaned_data.get('body')
            post_obj = Post(title=title, body=body, author_id=request.user.id)
            post_obj.save()
            messages.success(request, "Ok")
            return redirect(reverse("home:index"))
        else:
            messages.error(request, "Error")
            return redirect(reverse("blog:new"))
    else:
        form = forms.NewPostForm()
    return render(request, template_name='blog/new_post.html', context={'form': form})




@login_required
def get_users_posts(request: HttpRequest):
    user_posts = Post.objects.filter(author=request.user).all()
    print("\n\n", user_posts, "\n\n")
    return render(request, template_name='blog/user_posts.html', context={'items': user_posts})




class UserPostsListView(ListView):
    model = Post

    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        return Post.objects.filter(author=user)