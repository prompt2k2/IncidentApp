from import_export import resources
from .models import Incident

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
import os
from django.conf import settings
from django.contrib.staticfiles import finders

class IncidentResource(resources.ModelResource):
    class Meta:
        model = Incident
        
        
        


def link_callback(uri, rel):
    
    
    # result = finders.find(uri)
    # if result:
    #     if not isinstance(result, (list, tuple)):
    #         result = [result]
    #     result = list(os.path.realpath(path) for path in result)
    #     path = result[0]
    
    # else:
    #     # use short variable names
        sUrl = settings.STATIC_URL      # Typically /static/
        sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL       # Typically /static/media/
        mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/
        bRoot = settings.BASE_DIR       #Project's base directory

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        
        else:
            
            return uri
            #return os.path.join(bRoot, '../', uri)#uri

    # make sure that file exists
        if not os.path.isfile(path):
            raise Exception('media URI must start with %s or %s' % (sUrl, mUrl))
        return path


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    
    
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8", "ISO-8859-1")), result, link_callback=link_callback)
    
   
    
    
    if not pdf.err:
        #return HttpResponse(result.getvalue(), content_type='application/pdf') #return HTTP response.
        return result.getvalue() # returns the as pdf file.
    return None
    
    