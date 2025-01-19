from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpRequest


# Create your views here.


from students import forms
from students import models




def upload_file_view(request: HttpRequest):
    if request.method == "POST":
        form = forms.NewStudentFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_file_obj = models.StudentFile.objects.create(
                title=form.cleaned_data['title'],
                file=form.cleaned_data['file'],
                author_id=request.user.id
            )
            new_file_obj.save()
            messages.success(request, "File Saved")
            return redirect(reverse('home:index'))
    else:
        form = forms.NewStudentFileUploadForm()
    return render(request, 'students/new_file.html', {'form': form})