from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from cosmic_objects.models import *

# Register your models here.

admin.site.register(Constellation, ModelAdmin)
admin.site.register(AstronomicalObject, ModelAdmin)
admin.site.register(NebulaType, ModelAdmin)
admin.site.register(Star, ModelAdmin)
admin.site.register(Galaxy, ModelAdmin)
admin.site.register(Nebula, ModelAdmin)