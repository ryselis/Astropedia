# -*- coding: UTF-8 -*-
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
from django.forms.forms import Form
from django.forms.widgets import PasswordInput


class RegistrationForm(Form):
    username = CharField(label=u'Vartotojo vardas')
    password = CharField(label=u'Slaptažodis', widget=PasswordInput())
    password2 = CharField(label=u'Pakartokite slaptažodį', widget=PasswordInput())

    def clean_password2(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            raise ValidationError(u'Slaptažodžiai nesutampa')
        return self.cleaned_data['password2']