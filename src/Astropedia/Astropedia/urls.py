from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Astropedia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/', include('drawing.urls')),
    url(r'^admin/', include('cosmic_objects.urls')),
    url(r'^register', 'user_management.views.register'),
    url(r'^starmap', 'drawing.views.star_map'),
    url(r'^hr', 'drawing.views.hr'),
)
