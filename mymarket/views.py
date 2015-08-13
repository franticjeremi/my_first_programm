from django.http import HttpResponse
from django.shortcuts import render_to_response
'''from django.template import RequestContext, loader'''
import json
from .models import Mymarket

'''def index(request):
    template = loader.get_template('mymarket/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context),content_type="text/html")'''
def index(request):
    return render_to_response('mymarket/index.html')

def widgetsList(request):
    widgetsList = []
    
    for widget in Mymarket.objects.all().order_by('name'):
        widgetsList.append({'id': widget.id,'name': widget.name,'description': widget.description,'url': widget.url})
        
    data = json.dumps(widgetsList)
    return HttpResponse(data, content_type='application/javascript')