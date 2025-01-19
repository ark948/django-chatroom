from django import forms




from students.models import StudentFile





class NewStudentFileUploadForm(forms.ModelForm):
    class Meta:
        model = StudentFile
        fields = ('title', 'file')