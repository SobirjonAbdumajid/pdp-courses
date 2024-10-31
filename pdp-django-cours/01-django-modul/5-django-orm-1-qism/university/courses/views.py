from django.http import HttpResponse
from django.views import View

from .models import *
from django.shortcuts import render
from .forms import SpecialityForm, TeacherForm, SubjectForm

# Create your views here.
def index(request):
    name = request.GET.get('name', 'No speciality')
    return HttpResponse(f"Hello, {name}. You're at the index page.")


def specialities(request):

    specialities = Speciality.objects.all()
    if not specialities:
        # If no specialities exist, pass a message to the template
        return render(request, 'speciality.html', {'speciality': 'No speciality'})
    return render(request, template_name='speciality.html', context={'speciality': specialities})

def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'moduls.html', context={
        'teacher': teacher
    })

class TeacherApiView(View):
    # def get(self, request):
    #     name = request.GET.get('name', 'somsa')
    #     return render(request, template_name='somsajon.html', context={'name': name})

    def get(self, request):

        search = request.GET.get('search', '')
        all_teachers = Teacher.objects.all()
        if not search:
            return render(request, 'moduls.html', context={'modul': all_teachers})
        elif not all_teachers:
            return render(request, 'moduls.html', context={'modul': 'No teachers'})
        else:
            teacher = Teacher.objects.filter(first_name__icontains=search)
            return render(request, 'moduls.html', context={'modul':teacher})


def subject_detail(request, pk):
    # Try to get the subject by id. If it doesn't exist, return None.
    subject = Subject.objects.filter(id=pk).first()

    # If subject is None, display an error message
    if not subject:
        return render(request, 'subject_detail.html', {'message': 'Subject not found'})

    # Get related specialities and teachers for this subject
    specialities = subject.specialities.all()
    teachers = subject.teachers.all()

    # Render the template with subject details
    return render(request, 'subject_detail.html', {
        'subject': subject,
        'specialities': specialities,
        'teachers': teachers
    })

def subjects(request):
        # Fetch all subjects from the database
        subjects = Subject.objects.all()

        # If no subjects exist, send a message
        if not subjects:
            return render(request, 'moduls.html', {'message': 'No subjects'})

        # Render the template with the list of subjects
        return render(request, 'moduls.html', {'subjects': subjects})

    # def post(self, request):
    #     pass

def create_speciality(request):
    if request.method == 'GET':
        form = SpecialityForm()
    else:
        form = SpecialityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Speciality.objects.create(
                name=data['name'],
                code=data['code'],
                is_active=data['is_active'],
            )
    return render(request, 'create_speciality.html', {
        'form': form
    })

def teacher_create(request):
    if request.method == 'GET':
        form = TeacherForm()
    else:
        form = TeacherForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Teacher.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                degree=data['degree'],
            )
    return render(request, 'create_speciality.html', {
        'form': form
    })

# def subject_create(request):
#     if request.method == 'GET':
#         form = SubjectForm()
#     else:
#         form = SubjectForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Subject.objects.create(
#                 name=data['name'],
#                 specialities=data['specialities'],
#                 teachers=data['teachers'],
#             )
#     return render(request, 'create_speciality.html', {
#         'form': form
#     })

def subject_create(request):
    if request.method == 'GET':
        form = SubjectForm()
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Create the Subject instance first without many-to-many fields
            subject = Subject.objects.create(
                name=data['name']
            )

            # Now add the Many-to-Many fields using the set() method
            subject.specialities.set(data['specialities'])
            subject.teachers.set(data['teachers'])

    return render(request, 'create_speciality.html', {
        'form': form
    })
