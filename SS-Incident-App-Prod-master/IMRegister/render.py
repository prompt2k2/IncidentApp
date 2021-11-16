from io import BytesIO
from django.http import HttpResponse, response
from django.template.loader import get_template
from xhtml2pdf import pisa


class Render:
    
    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.errors:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF",  status=400)
        