from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import IMRegisterForms
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


@csrf_protect
def IncidentForm(request):
    
    if request.method == 'POST':
        form = IMRegisterForms(request.POST, request.FILES )
        
        if form.is_valid():
            name = request.POST.get('name')
            jobrole = request.POST.get('job_role')
            incitype = request.POST.get('incident_type')
            siteID = request.POST.get('siteID')
            site_name = request.POST.get('site_name')
            incident_date = request.POST.get('incident_date')
            incident_time = request.POST.get('incident_time')
            person_involved = request.POST.get('person_involved')
            describe = request.POST.get('incident_description')
            witness = request.POST.get('witness')
            loss = request.POST.get('loss')
            reported_to = request.POST.get('reported_to')
            date_reported = request.POST.get('date_reported')
            report_method = request.POST.get('report_method')            
            actions = request.POST.get('actions')
            #files = request.FILES('files')
            fullmessage = str([name.upper(), 
                               incitype, siteID, actions,
                               jobrole, site_name, incident_date,
                               incident_time, person_involved, 
                               describe, witness, loss,
                               reported_to, date_reported, report_method,
                               
                               ])
            
            try:
                send_mail('New Incident Report',
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
    #context = {}
    #context['form'] = IMRegisterForms()    
    return render(request, 'IMRegister/incident.html', {'form':form})
    

def Success(request):
     return render(request, 'IMRegister/success.html')