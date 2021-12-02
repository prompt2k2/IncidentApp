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
from django.template.loader import get_template
from django.template import Context, loader
from .models import Incident
from django.core.mail import EmailMessage
import random, imghdr
from django.views.generic import View
from .forms import IMRegisterForms
from IMRegister.resources import render_to_pdf, link_callback
from .models import Incident




@csrf_protect
def IncidentForm(request):
    
    if request.method == 'POST':
        form = IMRegisterForms(request.POST, request.FILES )
        
        if form.is_valid():
            subject = request.POST.get('site_name')
            managername = request.POST.get('manager') #this gets the key of the manager selected from the manager table.
            
            name = request.POST.get('name')
            job_role =  request.POST.get('job_role')
            incident_type = request.POST.get('incident_type')
            SiteID = request.POST.get('SiteID') 
            site_name = request.POST.get('site_name')
            incident_area = request.POST.get('incident_area')
            incident_area_detail = request.POST.get('incident_area_detail')
            direct_cause = request.POST.get('direct_cause')
            root_cause = request.POST.get('root_cause')
                        
            imme_action = request.POST.get('imme_action')
            imme_action_whom = request.POST.get('imme_action_whom')
            imme_action_when = request.POST.get('imme_action_when')
            long_action = request.POST.get('long_action')
            long_action_whom = request.POST.get('long_action_whom')
            long_action_when = request.POST.get('long_action_when')
                        
            imme_action2 = request.POST.get('imme_action2')
            imme_action2_whom = request.POST.get('imme_action2_whom')
            imme_action2_when = request.POST.get('imme_action2_when')
            long_action2 = request.POST.get('long_action2')
            long_action2_whom = request.POST.get('long_action2_whom')
            long_action2_when = request.POST.get('long_action2_when')
                        
            lost_hr = request.POST.get('lost_hr')
            incident_date = request.POST.get('incident_date')
            incident_time = request.POST.get('incident_time')
            person_involved = request.POST.get('person_involved')
            incident_description = request.POST.get('incident_description')
            witness = request.POST.get('witness')
            loss = request.POST.get('loss')
            reported_to = request.POST.get('reported_to') 
            date_reported = request.POST.get('date_reported') 
            report_method = request.POST.get('report_method')           
                        
            file1 = request.FILES.get('file1') 
            file2 = request.FILES.get('file2') 
            file3 = request.FILES.get('file3') 
            file4 = request.FILES.get('file4') 
           
                 
                 
                 
                
            lessons = request.POST.get('lessons') 
            
            
            for e in ManagerModel.objects.filter(id = managername): #Filters whatever the manager id is, and returns the email.
                
                cc_mail = e.email
            
            
            #for e in ManagerModel.objects.filter(id = managername): #Filters whatever the manager id is, and returns the email.
            template = loader.get_template('IMRegister/sheep.html')#Getting the template
            body = {
                'subject' : subject,
                'managername': managername,
                'name' : name, 
                'job_role': job_role, 
                'incident_type' : incident_type, 
                'SiteID' : SiteID, 
                'site_name' : site_name, 
                'incident_area': incident_area, 
                'incident_area_detail' : incident_area_detail, 
                'direct_cause' : direct_cause, 
                'root_cause' : root_cause, 
                        
                'imme_action' : imme_action, 
                'imme_action_whom' : imme_action_whom, 
                'imme_action_when' : imme_action_when, 
                'Llong_action' : long_action, 
                'long_action_whom': long_action_whom, 
                'long_action_when' : long_action_when, 
                        
                'imme_action2' : imme_action2, 
                'imme_actions2_whom' : imme_action2_whom, 
                'imme_action2_when' : imme_action2_when, 
                'long_action2' : long_action2, 
                'long_action_whom': long_action2_whom, 
                'long_action2_when': long_action2_when, 
                        
                'lost_hr' : lost_hr, 
                'incident_date' : incident_date, 
                'incident_time' : incident_time, 
                'person_involved': person_involved, 
                'incident_description' : incident_description, 
                'witness' : witness, 
                'loss':loss, 
                'reported_to': reported_to, 
                'date_reported' : date_reported, 
                'report_method' : request.POST.get('report_method'),#report_method ,           
                        
                'file1':file1, 
                'file2':file2, 
                'file3':file3, 
                'file4':file4, 
                
                'lessons':lessons, 
                }
            
            html = template.render(body)
            pdf = render_to_pdf('IMRegister/sheep.html', body)
            
            
            if pdf: 
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = 'New Incident at ' + subject +'.pdf'
                content = ('attachment; filename=', filename)
                response['Content-Disposition'] = content
                #return response
                
                #fullmessage = "\n".join(f'{i}:{j}' for i,j in body.items())
                
                bodymessage = "An incident report has been generated by " + name + " for " +subject + " " + SiteID+ "." + "\nSee attachement for full details." + "\n\n\n\nThis email and any attachments are confidential and may also be privileged. If you are not the intended recipient, please delete all copies immediately. \nYou may wish to refer to the incorporation details of Starsight Energy at https://www.starsightenergy.com"
                
                 
            
           
            
            
            
                try:
                    
                    email =EmailMessage(
                        
                        subject = subject,
                        body = bodymessage,
                        from_email = settings.EMAIL_HOST_USER,
                        to=['ppopoola@starsightenergy.com', cc_mail],
                        reply_to= [settings.EMAIL_HOST_USER],
                        headers = {'Message-ID':'Starsight IT Department ensures security of email sent from this application, but receivers are responsible for ensuring correctness and validity'},
                        
                        
                       
                    )
                    

                    email.attach(filename, pdf, 'application/pdf')
                    #email.attach_file(request.FILES.get('files') )
                    email.send()
                    
                                
                    form.save()
                    
                    
                    
                except BadHeaderError:
                    return HttpResponse("Invalid Header found")
                return HttpResponse(html)
                return HttpResponseRedirect("/success/")
                
            #form.save()
                
            
            #return HttpResponse(template.render(body))
        else:
            print(form.errors)
        
    else:
        form = IMRegisterForms()
   
    return render(request, 'IMRegister/incident.html', {'form':form})
    
    
    '''
    
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
                      ['ppopoola@starsightenergy.com', cc_mail],
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
    '''

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


#############################################################################################################################################################################################

# @csrf_protect
# def Confirmation(request):
#     if request.method == 'POST':
#         form = IMRegisterForms(request.POST, request.FILES )
        
#         message = get_template('IMRegister/sheep.html')
        
#         context = Context({'form':form})
        
    
#         mail = EmailMessage(
#             subject = 'New Incident Report',
#             body = message,
#             from_email = settings.EMAIL_HOST_USER,
#             to=['ppopoola@starsightenergy.com'],
#             reply_to=['itsupport@starsightenergy.com']
#         )
        
#         mail.content_subtype = 'html'
#         return mail.send()
    
#     else:
#         form = IMRegisterForms()
    
#     return render(request, 'IMRegister/sheep.html', {'form':form})

@csrf_protect
def Confirmation(request):
    template = loader.get_template('IMRegister/sheep.html')#Getting the template
    body = {
        'subject' : request.POST.get('site_name'),
        'incidentnumber': request.GET.get('incident_number'),
        'Name  ' : request.POST.get('name'), 
            'Job Role  ': request.POST.get('job_role'), 
            'Incident Type  ' : request.POST.get('incident_type'), 
            'SiteID  ' : request.POST.get('SiteID'), 
            'Site Name  ' : request.POST.get('site_name'), 
            'Incident Area   ' : request.POST.get('incident_area'), 
            'Incident Area Detail  ' : request.POST.get('incident_area_detail'), 
            'Direct Cause  ' : request.POST.get('direct_cause'), 
            'Root Cause  ' : request.POST.get('root_cause'), 
            
            'Immediate Action(s)  ' : request.POST.get('imme_action'), 
            'Immediate Action(s) by whom  ' : request.POST.get('imme_action_whom'), 
            'Immediate Action(s) when  ' : request.POST.get('imme_action_when'), 
            'Long Term Action(s)  ' : request.POST.get('long_action'), 
            'Long Term Action(s) by whom  ': request.POST.get('long_action_whom'), 
            'Long Term Action(s) when ' : request.POST.get('long_action_when'), 
            
            'Second Immediate Action(s)  ' : request.POST.get('imme_action2'), 
            'Second Immediate Action(s) by whom  ' : request.POST.get('imme_action2_whom'), 
            'Second Immediate Action(s) when  ' : request.POST.get('imme_action2_when'), 
            'Second Long Term Action(s)  ' : request.POST.get('long_action2'), 
            'Second Long Term Action(s) by whom  ': request.POST.get('long_action2_whom'), 
            'Second Long Term Action(s) when ' : request.POST.get('long_action2_when'), 
            
            'Lost Hour in Minutes  ' : request.POST.get('lost_hr'), 
            'Incident Date  ' : request.POST.get('incident_date'), 
            'Incident Time  ' : request.POST.get('incident_time'), 
            'Person(s) Involved  ': request.POST.get('person_involved'), 
            'Incident Description  ' : request.POST.get('incident_description'), 
            'Witness  ' : request.POST.get('witness'), "\n"
            'Material/Equipment Loss  ' : request.POST.get('loss'), 
            'Incident Report to:  ': request.POST.get('reported_to'), 
            'Incident Report on  ' : request.POST.get('date_reported'), 
            'Incident Report Method' : request.POST.get('report_method') ,           
            
            'Files Attached  ':request.FILES.get('files'), 
            'Lesson(s) Learned  ':request.POST.get('lessons'), 
    }
    return HttpResponse(template.render(body))