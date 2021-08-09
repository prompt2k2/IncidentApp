from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import IMRegisterForms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.views.generic import View
from .models import *
from .render import Render
from django.utils import timezone



@csrf_protect
def IncidentForm(request):
    
    if request.method == 'POST':
        form = IMRegisterForms(request.POST, request.FILES )
        
        if form.is_valid():
            subject = request.POST.get('site_name')
            body = {
            'name' : request.POST.get('name'),
            'jobrole': request.POST.get('job_role'),
            'incitype' : request.POST.get('incident_type'),
            'siteID' : request.POST.get('siteID'),
            'site_name' : request.POST.get('site_name'),
            'incident_date' : request.POST.get('incident_date'),
            'incident_time' : request.POST.get('incident_time'),
            'person_involved': request.POST.get('person_involved'),
            'describe' : request.POST.get('incident_description'),
            'witness' : request.POST.get('witness'),
            'loss' : request.POST.get('loss'),
            'reported_to': request.POST.get('reported_to'),
            'date_reported' : request.POST.get('date_reported'),
            'report_method' : request.POST.get('report_method') ,           
            'actions': request.POST.get('actions'),
            'files':request.FILES.get('files')
            }
            
            fullmessage = "\n".join(f'{i}:{j}' for i,j in body.items())
          
            
            try:
                send_mail(subject,
                          fullmessage,
                         
                      settings.EMAIL_HOST_USER,
                      ['ppopoola@starsightenergy.com'],
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
    #for item in incident:
        
        #type = item.siteID
        #name = item.name
        #place= item.site_name
        #meth= item.report_method
        
       
    return render(request, 'IMRegister/mail.html', {'incidentcount':incidentcount})
 

''' 
class Pdf(View):
    
    
    def get(self, request):
        incident = Incident.objects.all()
        params = {'incident': incident,
                  'request': request,}
        
        return Render.render('incidents.html', params)
'''