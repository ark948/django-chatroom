from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpRequest



# local imports
from blog.forms import AddPostForm, AddPostFormV2
from blog import forms



# markdownx
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



# summernote
def add_post_view_v2(request: HttpRequest):
    if request.method == "POST":
        form = AddPostFormV2(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "NICE")
            return redirect(reverse("home:index"))
        else:
            messages.error(request, "ERROR")
            return redirect(reverse("blog:add2"))
    else:
        form = AddPostFormV2()
    return render(request, template_name='blog/new_post_v2.html', context={"form": form})




def add_post_view_v3(request: HttpRequest):
    if request.method == "POST":
        form = forms.AddPostFormV3(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ok")
            return redirect(reverse("home:index"))
        else:
            messages.error(request, "Error")
            return redirect(reverse("blog:add3"))
    else:
        form = forms.AddPostFormV3()
    return render(request, template_name='blog/new_post_v3.html', context={'form': form})




def add_post_view_v4(request: HttpRequest):
    if request.method == "POST":
        form = forms.AddPostFormV4(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ok")
            return redirect(reverse("home:index"))
        else:
            messages.error(request, "Error")
            return redirect(reverse("blog:add4"))
    else:
        form = forms.AddPostFormV4()
    return render(request, template_name='blog/new_post_v4.html', context={'form': form})