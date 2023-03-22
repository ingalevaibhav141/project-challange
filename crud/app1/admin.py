from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Person

@admin.register(Person)
class personadmin(ImportExportActionModelAdmin):
    list_display=('name','email','location')
# Register your models here.
