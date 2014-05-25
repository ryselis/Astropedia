from django.shortcuts import render
import xmltodict
import json
from django.views.decorators.csrf import csrf_response_exempt

# Create your views here.
def render_star_map(request):
    pass

@csrf_response_exempt
def save_star_from_json(request):
    import pdb; pdb.set_trace()
    json_string = request.POST.get('Post')
    stars = json.loads(json_string)
    
def import_xml(request):
    xml_string = request.POST.get('xml')
    stars = xmltodict.parse(xml_string)
    