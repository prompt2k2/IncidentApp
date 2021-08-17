from django.db import models
from django.forms import ModelForm
from Managers.models import ManagerModel

INCIDENT_TYPES = [('Operations','Operations'),('OHSE','OHSE'), 
          ('Admin','Admin'),('IT','IT'), ('Security','Security')]

RM = [('Text Messages','Text Messages'),('Phone Call','Phone Call'),('Email','Email'),('This form', 'This form')]



class Incident(models.Model):
    
    incidentnumber = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Name (Surname First)', max_length=150)
    job_role = models.CharField(verbose_name='Job Role', max_length=90)
    incident_type= models.CharField(verbose_name='Incident Type', max_length=200, choices=INCIDENT_TYPES)
    SiteID = models.CharField(verbose_name='Site ID', max_length=6, null=True, blank=True)
    site_name = models.CharField(verbose_name='Site (Incident Location) Name',max_length=50)
    incident_area = models.CharField(verbose_name='Incident Area', max_length=50, null=True, blank=True)
    incident_area_detail = models.CharField(verbose_name='Incident Area description', max_length=250, null=True, blank=True)
    direct_cause = models.CharField(verbose_name='Direct Cause of Incident', max_length=200, null=True, blank=True)
    root_cause = models.CharField(verbose_name='Root Cause of Incident',max_length=400, null=True, blank=True)
    imme_action = models.CharField(verbose_name='Immediate action taken',max_length=200, null=True, blank=True)
    imme_action_whom = models.CharField(verbose_name='By whom', max_length=60, null=True, blank=True)
    imme_action_when = models.DateTimeField(verbose_name='When',null=True, blank=True)
    long_action = models.CharField(verbose_name='Long term action taken', max_length=600, null=True, blank=True)
    long_action_whom = models.CharField(verbose_name='By whom',max_length=60, null=True, blank=True)
    long_action_when = models.DateTimeField(verbose_name='When', null=True, blank=True)
    
    imme_action2 = models.CharField(verbose_name='Second Immediate action taken',max_length=200, null=True, blank=True)
    imme_action2_whom = models.CharField(verbose_name='By whom', max_length=60, null=True, blank=True)
    imme_action2_when = models.DateTimeField(verbose_name='When',null=True, blank=True)
    long_action2 = models.CharField(verbose_name='Second Long term action taken', max_length=600, null=True, blank=True)
    long_action2_whom = models.CharField(verbose_name='By whom',max_length=60, null=True, blank=True)
    long_action2_when = models.DateTimeField(verbose_name='When', null=True, blank=True)
    
    incident_date = models.DateTimeField(verbose_name='Incident Date', null=True, blank=True)
    incident_time = models.TimeField(verbose_name='Incident Time', null=True, blank=True)
    files = models.FileField(verbose_name='Attach Pictures', null=True, blank=True)
    person_involved = models.CharField(verbose_name='Person(s) involved in Incident',max_length=220)
    incident_description = models.CharField(verbose_name='Incident Description (Full Details)',max_length=2220)
    witness = models.CharField(verbose_name='Witness (if any)', max_length=220, null=True, blank=True)
    loss = models.CharField(verbose_name='Material/Equipment Loss (if any)',max_length=220, null=True, blank=True)
    reported_to = models.CharField(verbose_name='Reported to:', max_length=80, null=True, blank=True)
    date_reported = models.DateTimeField(verbose_name='Report Date',null=True, blank=True)
    report_method = models.CharField(verbose_name='Report Method',null=True, blank=True, max_length=20, choices=RM)
    lessons = models.CharField(verbose_name='Lesson(s) learned from Incident',max_length=2220, null=True, blank=True)
    lost_hr = models.IntegerField(verbose_name='Lost Hour',null=True, blank=True)
    manager = models.ForeignKey(ManagerModel, verbose_name='Manager', on_delete=models.DO_NOTHING, blank=False, max_length=30)
    

    
    def __str__(self):
        code = str(self.incidentnumber)
        return  code + "-"+ self.incident_type 
    
    
    