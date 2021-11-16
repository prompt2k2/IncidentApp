from django.contrib import admin
from .models import Incident
from import_export.admin import ImportExportModelAdmin

@admin.register(Incident)
class IncidentAdmin(ImportExportModelAdmin):
    
    class Meta:
        model = Incident


#admin.site.register(Incident)

