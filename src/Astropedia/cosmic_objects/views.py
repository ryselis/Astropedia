from django.shortcuts import render
import json

# Create your views here.
def render_star_map(request):
    pass

def save_star_from_json(request):
    json_string = request.POST.get('Post')
    stars = json.loads(json_string)
    import pdb; pdb.set_trace()