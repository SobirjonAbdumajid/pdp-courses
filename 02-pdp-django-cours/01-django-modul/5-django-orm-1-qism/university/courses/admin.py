from django.contrib import admin
from .models import Teacher, Speciality, Subject
from import_export.admin import ImportExportActionModelAdmin

# admin.site.register(Teacher)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name")
    list_display = ("first_name", "last_name", "degree")
    list_filter = ("degree",)
    # list_select_related = ("first_name", "last_name")

def check_if_specialities_are_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
    # queryset.filter(code="1111").update(is_active=True)

@admin.register(Speciality)
class SpecialityAdmin(ImportExportActionModelAdmin):
    search_fields = ("name", "code")
    list_display = ("name", "code", "is_active")
    actions = (check_if_specialities_are_active,)


# @admin.register(Subject)
# class SubjectAdmin(admin.ModelAdmin):
#     search_fields = ("name", "specialities", 'teachers')
#     list_display = ("name", "specialities", 'teachers')
#     # list_select_related = ("teachers", "specialities")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ("name", "specialities__name", "teachers__first_name", "teachers__last_name")

    # Enable autocomplete for 'specialities' and 'teachers' fields
    autocomplete_fields = ['specialities', 'teachers']

    list_display = ("name", "get_specialities", "get_teachers")

    def get_specialities(self, obj):
        return ", ".join([s.name for s in obj.specialities.all()])

    def get_teachers(self, obj):
        return ", ".join([t.first_name + " " + t.last_name for t in obj.teachers.all()])

    get_specialities.short_description = 'Specialities'
    get_teachers.short_description = 'Teachers'


