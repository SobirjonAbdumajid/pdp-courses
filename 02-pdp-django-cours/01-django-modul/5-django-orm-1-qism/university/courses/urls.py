from django.urls import path
from .views import *

urlpatterns = [
    # path('hello/<str:name>/', index, name='index'),
    path('hello/', index, name='index'),
    path('speciality/', specialities, name='specialities'),
    path('teacher/', TeacherApiView.as_view(), name='teacher'),
    path('teachers/<int:pk>/', teacher_detail, name='teacher_detail'),
    path('subject/', subjects, name='subjects'),  # List of all subjects
    path('subject/<int:pk>/', subject_detail, name='subject_detail'),  # Detail for a specific subject
    path('speciality/create/', create_speciality, name='create_speciality'),
    path('teacher/create/', teacher_create, name='teacher_create'),
    path('subject/create/', subject_create, name='subject_create')
]
