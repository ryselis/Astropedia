from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^cosmic_objects/parse_stars$', 'cosmic_objects.views.save_star_from_json')
) 