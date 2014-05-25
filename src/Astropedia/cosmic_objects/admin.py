from django.contrib import admin
from contrib.options import CustomModelAdmin
from django.contrib.admin.options import ModelAdmin
from cosmic_objects.models import *
from django.http import HttpResponseRedirect
import os

# Register your models here.

def sync(request, queryset, modeladmin):
    os.system("php " + os.path.dirname(os.path.realpath(__file__)) + "../PHP/parse_stars.php")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

class StarAdmin(CustomModelAdmin):
    actions = [sync]
    

admin.site.register(Constellation, ModelAdmin)
admin.site.register(AstronomicalObject, ModelAdmin)
admin.site.register(NebulaType, ModelAdmin)
admin.site.register(Star, StarAdmin)
admin.site.register(Galaxy, ModelAdmin)
admin.site.register(Nebula, ModelAdmin)