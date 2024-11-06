from django import forms
from .models import Speciality, Teacher

class SpecialityForm(forms.Form):
    name = forms.CharField(max_length=200)
    code = forms.CharField(max_length=200)
    is_active = forms.BooleanField(required=False)

class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=255)
    degree = forms.CharField(max_length=100)

class SubjectForm(forms.Form):
    name = forms.CharField(max_length=255)
    specialities = forms.ModelMultipleChoiceField(queryset=Speciality.objects.all())
    teachers = forms.ModelMultipleChoiceField(queryset=Teacher.objects.all())



# class Subject(models.Model):
#     name = models.CharField(max_length=255)
#     specialities = models.ManyToManyField(Speciality)
#     teachers = models.ManyToManyField(Teacher)