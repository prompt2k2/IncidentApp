from django.forms import ModelForm, Textarea,DateInput,ClearableFileInput, TimeInput, CheckboxSelectMultiple, NumberInput, TextInput, RadioSelect
from .models import Incident


class IMRegisterForms(ModelForm):
    
    class Meta:
        model = Incident
        fields = '__all__'
        widgets = {
            
            'name' : Textarea(attrs={'rows':1,'placeholder':'Name of person completing this form'}),
            'job_role' : TextInput (attrs={'placeholder':"e.g Site Engineer"}),
            'SiteID' : TextInput(attrs={'placeholder':"Site ID"}),
            'site_name' :Textarea(attrs={'rows':3,'placeholder':"Indicate Site or Location of incident"}),
            'incident_date':DateInput (attrs={'type':'date'}),
            'incident_time':TimeInput (attrs={'type':'time'}),
            'person_involved' :Textarea( attrs={'rows':3,'placeholder':'State Name, Contacts of person(s) involved in this incident (IF ANY)'}),
            'incident_description' :Textarea( attrs={'rows':3}),
            'witness' :Textarea(attrs={'rows':3, 'placeholder':'Names and Contacts of those present during the incident (IF ANY)'}),
            'loss' : Textarea (attrs={'rows':4, 'placeholder':'List names and types of loss in this incident'}),
            'reported_to' : TextInput( ),
            'date_reported' :DateInput(attrs={'type':'date'}),
            'incident_area' :Textarea(attrs={'rows':3, 'placeholder': 'e.g DB, Generator area, etc'}),
            'files' :ClearableFileInput(attrs={'multiple':True}),
            'incident_area_detail' : Textarea(attrs={'rows':3, 'placeholder':"Incident area within the premises"}),
            'direct_cause' : Textarea(attrs={'rows':3,'placeholder':'State incident direct cause'}),
            'root_cause' : Textarea(attrs={'rows':3,'placeholder':'State incident root cause'}),
            
            'imme_action': Textarea(attrs={'rows':4,'placeholder':'Immediate action taken'}),
            'imme_action_whom' : TextInput(attrs={'placeholder':'By Whom'}),
            'imme_action_when' : DateInput(attrs={'type':'date'}),
            'long_action' : Textarea(attrs={'rows':4,'placeholder':'Long term action(s) planned/actioned'}),
            'long_action_whom' : TextInput(attrs={'placeholder':'By Whom'}),
            'long_action_when' : DateInput(attrs={'type':'date'}),
            
            'imme_action2': Textarea(attrs={'rows':4,'placeholder':'Immediate action taken'}),
            'imme_action2_whom' : TextInput(attrs={'placeholder':'By Whom'}),
            'imme_action2_when' : DateInput(attrs={'type':'date'}),
            'long_action2' : Textarea(attrs={'rows':4,'placeholder':'Long term action(s) planned/actioned'}),
            'long_action2_whom' : TextInput(attrs={'placeholder':'By Whom'}),
            'long_action2_when' : DateInput(attrs={'type':'date'}),
            
            'lessons': Textarea(attrs={'rows':3, 'placeholder':'describe in details lesson(s) learned from this incident'}),
            'lost_hr': NumberInput(attrs={'placeholder':'Numbers only'})

        }
        
        def __init__(self, *args, **kwargs):
            super(IMRegisterForms, self).__init__(*args, **kwargs)
            self.fields['report_method'].empty_label='Select'
            self.fields['incident_type'].empty_label='Select'

    
    
    
        
  