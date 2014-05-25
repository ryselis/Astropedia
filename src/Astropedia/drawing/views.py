from django.shortcuts import render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def star_map(request):
    return render_to_response('drawing/BUILD.html')


@csrf_exempt
def hr(request):
    return render_to_response('drawing/hr.html')