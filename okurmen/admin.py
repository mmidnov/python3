# okurmen/admin.py
from django.contrib import admin
from .models import Student, Teacher, Group, Manager

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'payment', 'payment_date', 'manager')
    search_fields = ('name', 'number', 'manager__name')
    list_filter = ('payment_date', 'manager')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name','programming_type')
    search_fields = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'trainer', 'mentor', 'start_date', 'end_date')
    search_fields = ('name', 'trainer', 'mentor')

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'responsibilities', 'directed_students_count', 'manager_number')
    search_fields = ('name', 'responsibilities', 'manager_number')
