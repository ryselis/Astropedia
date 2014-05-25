from django.contrib.auth.models import User, Group
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from user_management.forms import RegistrationForm
from user_management.models import UserSubmittedInfo


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'],
                                            )
            user.is_staff = True
            user.save()
            group = Group.objects.get(name=u'Registruotas vartotojas')
            group.user_set.add(user)
            group.save()
            return HttpResponseRedirect('/admin')
        return HttpResponseRedirect('/register')
    else:
        form = RegistrationForm()
        parameters = {'form': form}
        return render_to_response('registration/registration_form.html', parameters,
                                  context_instance=RequestContext(request))


def get_user_rating(user):
    submission_total = UserSubmittedInfo.objects.filter(user=user).count()
    submission_accepted = UserSubmittedInfo.objects.filter(user=user,
                                                           status=UserSubmittedInfo.STATUS_ACCEPTED).count()
    if not submission_total:
        return 0
    return 100 * float(submission_accepted) / float(submission_total)