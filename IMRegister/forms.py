from django import forms

office = [('Operations','Operations'),('OHSE','OHSE'), 
          ('Admin','Admin'),('IT','IT'), ('Security','Security')]

RM = [('Text Messages','Text Messages'),('Phone Call','Phone Call'),('Email','Email'),('This form', 'This form')]

class IMRegisterForms(forms.Form):
    
    name = forms.CharField(label="Full Name", widget=forms.Textarea(attrs={'rows':3,'placeholder':'Name of person completing this form'}),max_length=80)
    job_role = forms.CharField(label="Job Role", max_length=30)
    incident_type= forms.MultipleChoiceField(label="Incident Type", required=True, widget=forms.CheckboxSelectMultiple, choices=office, )
    siteID = forms.CharField(label="Site ID", max_length=6, required=False)
    site_name = forms.CharField(label="Site (Location) Name", widget=forms.Textarea(attrs={'rows':3,'placeholder':'Indicate Site or Location of incident'}),max_length=50, required=False)
    incident_date = forms.DateTimeField(label="Incident Date", widget=forms.DateInput(attrs={'type':'date'}))
    #incident_time = forms.DateTimeField(label="Incident Time", required=False,widget=forms.DateInput(attrs={'type':'time'}))
    person_involved = forms.CharField(label="Person(s) Involved", widget=forms.Textarea(attrs={'rows':3,'placeholder':'State Name, Contacts of person(s) involved in this incident (IF ANY)'}))
    incident_description = forms.CharField(label="Incident Description", widget=forms.Textarea(attrs={'rows':5}))
    witness = forms.CharField(label="Witness(es)", widget=forms.Textarea(attrs={'rows':3, 'placeholder':'Names and Contacts of those present during the incident (IF ANY)'}))
    loss = forms.CharField(label="Item(s)/Material(s) Loss ", required=False, widget=forms.Textarea(attrs={'rows':4, 'placeholder':'List names and types of loss in this incident'}))
    reported_to = forms.CharField(label="Reported To", max_length=80)
    date_reported = forms.DateTimeField(label="Date Reported", widget=forms.DateInput(attrs={'type':'date'}))
    report_method = forms.ChoiceField(label="Report Method", required=True, widget=forms.RadioSelect, choices=RM)
    actions = forms.CharField(label="Action(s) Taken", required=False, widget=forms.Textarea(attrs={'rows':3, 'placeholder': 'Describe any action(s) taken'}))
    
    
    def __str__(self):
        return self.incident_type