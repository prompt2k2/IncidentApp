from import_export import resources
from .models import Incident

class IncidentResource(resources.ModelResource):
    class Meta:
        model = Incident