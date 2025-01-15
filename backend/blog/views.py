from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpRequest



# local imports
from blog.forms import AddPostForm



def add_post_view(request: HttpRequest):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "NICE")
            return redirect(reverse("home:index"))
        else:
            messages.error(request, "ERROR")
            return redirect(reverse("blog:add"))
    else:
        form = AddPostForm()
    return render(request, template_name='blog/new_post.html', context={"form": form})
