from django.shortcuts import render
from .forms import IMRegisterForms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def IncidentForm(request):
    
    
    context = {}
    context['form'] = IMRegisterForms()    
    return render(request, 'IMRegister/incident.html', context)
    
def sendEmail(request):
    
    if request.method == 'POST':
        form = IMRegisterForms(request.POST)
        if form.is_valid():
            subject = "Incident Report"
            body = {form}
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'prompt2k2@gmail.com', ['prompt2k2@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            
    form = IMRegisterForms()
    return render(request, 'IMRegister/incident.html', {'form':form})