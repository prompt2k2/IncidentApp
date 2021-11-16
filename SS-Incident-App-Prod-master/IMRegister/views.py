from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import IMRegisterForms
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views.generic import View
from .models import *
from .render import Render
from django.utils import timezone
from .resources import IncidentResource
from django.db.models import Sum
from Managers.models import ManagerModel




@csrf_protect
def IncidentForm(request):
    
    if request.method == 'POST':
        form = IMRegisterForms(request.POST, request.FILES )
        
        if form.is_valid():
            subject = request.POST.get('site_name')
            managername = request.POST.get('manager') #this gets the key of the manager selected from the manager table.
            
            
            for e in ManagerModel.objects.filter(id = managername): #Filters whatever the manager id is, and returns the email.
                
                cc_mail = e.email
              
            
            
            body = {
            'Name  ' : request.POST.get('name'), "\n"
            'Job Role  ': request.POST.get('job_role'), "\n"
            'Incident Type  ' : request.POST.get('incident_type'), "\n"
            'SiteID  ' : request.POST.get('SiteID').upper(), "\n"
            'Site Name  ' : request.POST.get('site_name'), "\n"
            'Incident Area   ' : request.POST.get('incident_area'), "\n"
            'Incident Area Detail  ' : request.POST.get('incident_area_detail'), "\n"
            'Direct Cause  ' : request.POST.get('direct_cause'), "\n"
            'Root Cause  ' : request.POST.get('root_cause'), "\n"
            
            'Immediate Action(s)  ' : request.POST.get('imme_action'), "\n"
            'Immediate Action(s) by whom  ' : request.POST.get('imme_action_whom'), "\n"
            'Immediate Action(s) when  ' : request.POST.get('imme_action_when'), "\n"
            'Long Term Action(s)  ' : request.POST.get('long_action'), "\n"
            'Long Term Action(s) by whom  ': request.POST.get('long_action_whom'), "\n"
            'Long Term Action(s) when ' : request.POST.get('long_action_when'), "\n"
            
            'Second Immediate Action(s)  ' : request.POST.get('imme_action2'), "\n"
            'Second Immediate Action(s) by whom  ' : request.POST.get('imme_action2_whom'), "\n"
            'Second Immediate Action(s) when  ' : request.POST.get('imme_action2_when'), "\n"
            'Second Long Term Action(s)  ' : request.POST.get('long_action2'), "\n"
            'Second Long Term Action(s) by whom  ': request.POST.get('long_action2_whom'), "\n"
            'Second Long Term Action(s) when ' : request.POST.get('long_action2_when'), "\n"
            
            'Lost Hour in Minutes  ' : request.POST.get('lost_hr'), "\n"
            'Incident Date  ' : request.POST.get('incident_date'), "\n"
            'Incident Time  ' : request.POST.get('incident_time'), "\n"
            'Person(s) Involved  ': request.POST.get('person_involved'), "\n"
            'Incident Description  ' : request.POST.get('incident_description'), "\n"
            'Witness  ' : request.POST.get('witness'), "\n"
            'Material/Equipment Loss  ' : request.POST.get('loss'), "\n"
            'Incident Report to:  ': request.POST.get('reported_to'), "\n"
            'Incident Report on  ' : request.POST.get('date_reported'), "\n"
            'Incident Report Method' : request.POST.get('report_method') ,  "\n"         
            
            'Files Attached  ':request.FILES.get('files'), "\n"
            'Lesson(s) Learned  ':request.POST.get('lessons'),
            }
            
            fullmessage = "\n".join(f'{i}:{j}' for i,j in body.items())
            
            
            
            try:
                send_mail(subject,
                          fullmessage,
                         
                      settings.EMAIL_HOST_USER,
                      ['customerservice@starsightenergy.com', cc_mail],
                      fail_silently=False)
                               
                form.save()
                
            except BadHeaderError:
                return HttpResponse("Invalid Header found")
            return HttpResponseRedirect("/success/")
        
        else:
            print(form.errors)
        
    else:
        form = IMRegisterForms()
   
    return render(request, 'IMRegister/incident.html', {'form':form})
    

def Success(request):
     return render(request, 'IMRegister/success.html')
 
def Frontend(request):
    
    incidentcount = Incident.objects.all().count
    incident = Incident.objects.all()
    losthours = Incident.objects.all().aggregate(Sum('lost_hr'))['lost_hr__sum']
    context = {'incidentcount': incidentcount,
               'losthours':losthours}  
    return render(request, 'IMRegister/mail.html', context)
 

def exportfile(request):
    incident_resource = IncidentResource()
    dataset = incident_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Incidents.csv"'
    return response
