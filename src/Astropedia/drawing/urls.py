from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^drawing/star_map$', 'drawing.views.render_star_map')
) 