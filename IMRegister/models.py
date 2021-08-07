from django.db import models
from django.forms import ModelForm


# Create your models here.

class Incident(models.Model):
    
    incidentnumber = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    job_role = models.CharField(max_length=90)
    incident_type= models.CharField(max_length=200)
    siteID = models.CharField(max_length=6, null=True, blank=True)
    site_name = models.CharField(max_length=50)
    incident_date = models.DateTimeField()
    incident_time = models.TimeField()
    files = models.FileField(null=True, blank=True)
    person_involved = models.CharField(max_length=220)
    incident_description = models.CharField(max_length=220)
    witness = models.CharField(max_length=220, null=True, blank=True)
    loss = models.CharField(max_length=220, null=True, blank=True)
    reported_to = models.CharField(max_length=80)
    date_reported = models.DateTimeField()
    report_method = models.CharField(max_length=20)
    actions = models.CharField(max_length=220, null=True, blank=True)
    
    def __str__(self):
        code = str(self.incidentnumber)
        return  code + "-"+ self.incident_type 
    
    