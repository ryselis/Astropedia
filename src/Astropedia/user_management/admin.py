# -*- coding: UTF-8 -*-
from django.contrib import admin, messages
from django.contrib.admin.views.main import ChangeList
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from django.http.response import HttpResponseRedirect
from contrib.options import CustomModelAdmin
from user_management.models import ScientistsAsks

# Register your models here.
from user_management.views import get_user_rating


def ask_to_be_a_scientist(modeladmin, request, queryset):
    user = request.user
    if user.groups.filter(name=u'Registruotas vartotojas').count() > 0:
        status = ScientistsAsks.STATE_UNCONFIRMED
        ScientistsAsks.objects.create(user=user, status=status)
    else:
        messages.warning(request, u'Jūs jau esate mokslininkas')
    return HttpResponseRedirect('/admin/user_management/scientistsasks/')


def confirm(modeladmin, request, queryset):
    user = request.user
    if user.groups.filter(name=u'Mokslininkas').count() > 0:
        for obj in queryset:
            if obj.status == ScientistsAsks.STATE_UNCONFIRMED:
                obj.status = ScientistsAsks.STATE_CONFIRMED
                obj.save()
                obj.user.is_staff = True
                obj.user.is_superuser = True
                obj.user.save()
                g = Group.objects.get(name=u'Registruotas vartotojas')
                g.user_set.remove(obj.user)
                g.save()
                g = Group.objects.get(name=u'Mokslininkas')
                g.user_set.add(obj.user)
                g.save()
    else:
        messages.warning(request, u'Tik mokslininkas gali patvirtinti prašymą')
    return HttpResponseRedirect('/admin/user_management/scientistsasks/')


def reject(modeladmin, request, queryset):
    user = request.user
    if user.groups.filter(name=u'Mokslininkas').count() > 0:
        for obj in queryset:
            if obj.status == ScientistsAsks.STATE_UNCONFIRMED:
                obj.status = ScientistsAsks.STATE_REJECTED
                obj.save()
    else:
        messages.warning(request, u'Tik mokslininkas gali atmesti prašymą')
    return HttpResponseRedirect('/admin/user_management/scientistsasks/')


class ScientistsAsksAdmin(CustomModelAdmin):
    def has_add_permission(self, request):
        return False

    def get_queryset(self, request):
        qs = CustomModelAdmin.get_queryset(self, request)
        if request.user.groups.filter(name=u'Mokslininkas').count() == 0:
            qs = qs.filter(user=request.user)
        return qs

    def get_changelist(self, request, **kwargs):
        class ScientistChangeList(ChangeList):
            def url_for_result(self, result):
                return '#'

        return ScientistChangeList

    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.list_display_links = (None,)

    def has_delete_permission(self, request, obj=None):
        return False

    actions = [ask_to_be_a_scientist, confirm, reject]
    list_display = ['user', 'status']
    list_filter = ['status']


class CustomUserAdmin(UserAdmin):
    list_display = list(UserAdmin.list_display) + ['get_user_rating']

    def get_user_rating(self, obj):
        return unicode(get_user_rating(obj)) + u'%'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(ScientistsAsks, ScientistsAsksAdmin)
# admin.site.register(UserSubmittedInfo, CustomModelAdmin)