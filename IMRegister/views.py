from django.shortcuts import render
from .forms import IMRegisterForms
from django.http import HttpResponseRedirect


def IncidentForm(request):
    
    if request.method == 'POST':
        form = IMRegisterForms(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/success/")
    
    
    else:
        form = IMRegisterForms()
    #context = {}
    #context['form'] = IMRegisterForms()    
    return render(request, 'IMRegister/incident.html', {'form':form})
    

def Success(request):
     return render(request, 'IMRegister/success.html')