from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ManagerModel
from .forms import ManagerForm

def ManagerVForm(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST) #create a form and fill with request data
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mlist/') #points to the urls.py path
        else:
            form.errors
            sender = repr(form.errors)
            print (repr(form.errors))
            return HttpResponse(sender)
    else:
        form = ManagerForm()
        context = {'form': form}
    return render(request, "Managers/managers.html", context )
        
 


def ManagerList(request):
    context = {'mgr':ManagerModel.objects.all()}
    return render(request, "Managers/managerlist.html", context)