from django.forms import ModelForm, Textarea,DateInput,ClearableFileInput, TimeInput, CheckboxSelectMultiple, NumberInput, TextInput, RadioSelect
from .models import Incident

INCIDENT_TYPES = [('Operations','Operations'),('OHSE','OHSE'), 
          ('Admin','Admin'),('IT','IT'), ('Security','Security')]

RM = [('Text Messages','Text Messages'),('Phone Call','Phone Call'),('Email','Email'),('This form', 'This form')]

class IMRegisterForms(ModelForm):
    
    class Meta:
        model = Incident
        fields = '__all__'
        widgets = {
            
            'name' : Textarea(attrs={'rows':1,'placeholder':'Name of person completing this form'}),
            'job_role' : TextInput (attrs={'placeholder':"e.g Site Engineer"}),
            'incident_type':CheckboxSelectMultiple (attrs={'placeholder':"Incident Type"}, choices=INCIDENT_TYPES),
            'siteID' : TextInput(attrs={'placeholder':"Site ID"}),
            'site_name' :Textarea(attrs={'rows':3,'placeholder':"Indicate Site or Location of incident"}),
            'incident_date':DateInput (attrs={'type':'date'}),
            'incident_time':TimeInput (attrs={'type':'time'}),
            'person_involved' :Textarea( attrs={'rows':3,'placeholder':'State Name, Contacts of person(s) involved in this incident (IF ANY)'}),
            'incident_description' :Textarea( attrs={'rows':5}),
            'witness' :Textarea(attrs={'rows':3, 'placeholder':'Names and Contacts of those present during the incident (IF ANY)'}),
            'loss' : Textarea (attrs={'rows':4, 'placeholder':'List names and types of loss in this incident'}),
            'reported_to' : TextInput( ),
            'date_reported' :DateInput(attrs={'type':'date'}),
            'report_method'  :RadioSelect(choices=RM),
            'incident_area' :Textarea(attrs={'rows':3, 'placeholder': 'e.g DB, Generator area, etc'}),
            'files' :ClearableFileInput(attrs={'multiple':True}),
            'incident_area_detail' : Textarea(attrs={'rows':3, 'placeholder':"Incident area within the premises"}),
            'direct_cause' : Textarea(attrs={'rows':4,'placeholder':'State incident direct cause'}),
            'root_cause' : Textarea(attrs={'rows':4,'placeholder':'State incident root cause'}),
            'imme_action': Textarea(attrs={'rows':4,'placeholder':'Immediate action taken'}),
            'imme_action_whom' : TextInput(attrs={'placeholder':'By Whom'}),
            'imme_action_when' : DateInput(attrs={'type':'date'}),
            'long_action' : Textarea(attrs={'rows':4,'placeholder':'Long term action(s) planned/actioned'}),
            'long_action_whom' : TextInput(attrs={'placeholder':'By Whome'}),
            'long_action_when' : DateInput(attrs={'type':'date'}),
            'lessons': Textarea(attrs={'placeholder':'describe in details lesson(s) learned from this incident'}),
            'lost_hr': NumberInput(attrs={'placeholder':'In minutes'})

        }

    
    
    
        
  