from django.contrib import admin
from user_management.models import *
from django.contrib.admin.options import ModelAdmin

# Register your models here.

admin.site.register(ScientistsAsks, ModelAdmin)
admin.site.register(UserSubmittedInfo, ModelAdmin)