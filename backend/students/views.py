from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, FileResponse
import magic


# Create your views here.


from students import forms
from students import models




@login_required
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




@login_required
def view_user_files(request: HttpRequest):
    user_files = request.user.files.all()
    return render(request, template_name='students/files_list.html', context={'items': user_files})




def file_path_mime(file_path):
    mime = magic.from_file(file_path, mime=True)
    return mime




@login_required
def view_file(request: HttpRequest, item_id=None):
    f = magic.Magic(uncompress=False, mime=True)
    file_obj = models.StudentFile.objects.get(id=item_id)
    if file_obj.author.id == request.user.id:
        mime = f.from_file(file_obj.file.path)
        print("\n\n", mime, "\n\n")
        if mime == "text/plain":
            return HttpResponse(file_obj.file, content_type='text/plain')
        elif mime == "image/jpeg":
            return FileResponse(file_obj.file)
        return HttpResponse("OK")
    else:
        return HttpResponse("File does not belong to you.")