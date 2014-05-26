from django.shortcuts import render_to_response

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


@csrf_exempt
def star_map(request):
    return HttpResponseRedirect('http://paukau.stud.if.ktu.lt/ftp/ASTROPEDIA/BUILD.html')


@csrf_exempt
def hr(request):
    return HttpResponseRedirect('http://paukau.stud.if.ktu.lt/ftp/ASTROPEDIA1/BUILD.html')