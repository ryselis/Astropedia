from django.contrib import admin, messages
from django.contrib.admin.views.main import ChangeList
from contrib.options import CustomModelAdmin
from django.contrib.admin.options import ModelAdmin
from cosmic_objects.models import *
from django.http import HttpResponseRedirect
import os

# Register your models here.


def sync(modeladmin, request, queryset):
    os.popen("php " + os.path.dirname(os.path.realpath(__file__)) + "/../PHP/parse_stars.php").read()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def confirm(modeladmin, request, queryset):
    if request.user.groups.filter(name=u'Mokslininkas').count() == 0:
        messages.warning(request, u'Tik mokslininkas gali patvirtinti kosminius objektus')
    else:
        for q in queryset:
            if q.user_submission and q.user_submission.status == UserSubmittedInfo.STATUS_PENDING:
                q.user_submission.status = UserSubmittedInfo.STATUS_ACCEPTED
                q.user_submission.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AstronomicalObjectAdmin(CustomModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj:
            return request.user.groups.filter(name=u'Mokslininkas').count() > 0
        return CustomModelAdmin.has_change_permission(self, request, obj)

    def save_model(self, request, obj, form, change):
        obj.save()
        if request.user.groups.filter(name=u'Mokslininkas').count() == 0:
            user_submitted_info = UserSubmittedInfo.objects.create(status=UserSubmittedInfo.STATUS_PENDING,
                                                                   user=request.user,
                                                                   odjecktId=obj.id)
            obj.user_submission = user_submitted_info
            obj.save()

    list_display = ['name', 'constellation', 'visible_magnitude']
    actions = [confirm]


class StarAdmin(AstronomicalObjectAdmin):
    actions = AstronomicalObjectAdmin.actions + [sync]
    list_filter = ['constellation',  'user_submission__status']
    list_display = ['name', 'constellation', 'visible_magnitude', 'absolute_magnitude', 'get_submission_status']


admin.site.register(Constellation, CustomModelAdmin)
#admin.site.register(AstronomicalObject, CustomModelAdmin)
admin.site.register(NebulaType, CustomModelAdmin)
admin.site.register(Star, StarAdmin)
admin.site.register(Galaxy, AstronomicalObjectAdmin)
admin.site.register(Nebula, AstronomicalObjectAdmin)
admin.site.register(Planet, CustomModelAdmin)