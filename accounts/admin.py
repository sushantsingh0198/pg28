from django.contrib import admin
from accounts.models import TeacherDetail, ClassDetail
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(TeacherDetail)
class TeacherDetail(ImportExportModelAdmin):
    pass


class TeacherDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'e_code', "available_load")

@admin.register(ClassDetail)
class ClassDrtail(ImportExportModelAdmin):
    pass


class ClassDetailAdmin(ClassDetail):
    list_display = ('sem', 'cls')