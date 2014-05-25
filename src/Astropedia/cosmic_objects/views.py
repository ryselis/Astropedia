from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
import xmltodict
import json

# Create your views here.
from cosmic_objects.models import Star, Constellation, AstronomicalObject


def render_star_map(request):
    pass


@csrf_exempt
def save_star_from_json(request):
    json_string = request.POST.get('Post')
    stars = json.loads(json_string)
    import_datadict(stars)
    return HttpResponse('OK')


@csrf_exempt
def import_xml(request):
    xml_string = request.POST.get('xml')
    stars = xmltodict.parse(xml_string)
    import_datadict(stars)
    return HttpResponse('OK')


def import_datadict(datadict):
    for star in datadict:
        try:
            absolute_magnitude = unicode_to_float(star[u'Absolute magnitude'])
            distance = unicode_to_float(star[u'Stellar distance'])
            visible_magnitude = unicode_to_float(star[u'Apparent magnitude'])
            rascention = parse_rascension(star[u'Right ascension'])
            declination = parse_declination(star[u'Declination'])
            spectral_class = star[u'Stellar classification']
            proper_name = star[u'Proper names (astronomy)'].replace('(page does not exist)', '')
            constellation_name = star[u'Constellation']
            constellation = Constellation.objects.filter(name=constellation_name)
            if constellation.count() > 0:
                constellation = constellation[0]
            else:
                constellation = Constellation.objects.create(name=constellation_name,
                                                             abbreviation=constellation_name[:3])
            if not Star.objects.filter(rectascence=rascention, declination=declination).exists():
                s = Star.objects.create(constellation=constellation, rectascence=rascention, declination=declination,
                                        distance=distance, visible_magnitude=visible_magnitude, name=proper_name,
                                        type=AstronomicalObject.TYPE_STAR, absolute_magnitude=absolute_magnitude,
                                        spectral_class=spectral_class, brightness=-1, visible_magnitude_amplitude=0,
                                        mass=-1)
                LogEntry.objects.create(user=User.objects.get(username='system'),
                                        content_type=ContentType.objects.get_for_model(Star),
                                        object_id=unicode(s.id), object_repr=unicode(s), action_flag=ADDITION,
                                        change_message=u'Imported from XML/Json')
        except:
            pass


def unicode_to_float(uni_str):
    return float(uni_str.replace(u'\u2212', '-'))


def parse_rascension(uni_str):
    parts = uni_str.split('h')
    hours = int(parts[0])
    parts = parts[1].split('m')
    minutes = float(parts[0])
    parts = parts[1].split('s')
    seconds = float(parts[0])
    return hours + minutes / 60 + seconds / 3600


def parse_declination(uni_str):
    parts = uni_str.split(u'\xb0')
    hours = int(parts[0])
    parts = parts[1].split(u'\u2032')
    minutes = float(parts[0])
    parts = parts[1].split(u'\u2033')
    seconds = float(parts[0])
    return hours + minutes / 60 + seconds / 3600