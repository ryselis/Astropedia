from django.conf.urls import patterns

urlpatterns = patterns('',
    url(r'^drawing/star_map$', 'drawing.views.render_star_map')
) 