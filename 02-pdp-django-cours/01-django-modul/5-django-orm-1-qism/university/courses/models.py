from django.db import models
from datetime import datetime

class Speciality(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    start_data = models.DateField(default=datetime.now, null=True, blank=True)  # Corrected this line
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, {self.code}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}"

class Subject(models.Model):
    name = models.CharField(max_length=255)
    specialities = models.ManyToManyField(Speciality)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f"{self.name}"
