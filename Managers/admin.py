from django.contrib import admin
from .models import ManagerModel
from import_export.admin import ImportExportModelAdmin

@admin.register(ManagerModel)
class ManagerAdmin(ImportExportModelAdmin):
    
    class Meta:
        model = ManagerModel