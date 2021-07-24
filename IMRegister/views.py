from django.shortcuts import render
from .forms import IMRegisterForms


def IncidentForm(request):
    
    
    context = {}
    context['form'] = IMRegisterForms()    
    return render(request, 'IMRegister/incident.html', context)
    
