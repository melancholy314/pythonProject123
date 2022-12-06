from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Student name', {'fields': ['name']}),
        ('Student surname', {'fields': ['surname']}),
        ('Student group', {'fields': ['group']})
    ]

admin.site.register(Student, StudentAdmin)