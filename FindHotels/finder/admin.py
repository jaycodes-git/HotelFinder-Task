from django.contrib import admin
from .models import Hotel
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Hotel)
class ViewAdmin(ImportExportModelAdmin):
    pass
    

