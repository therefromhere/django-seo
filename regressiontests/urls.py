from django.conf.urls import include

from django.contrib import admin
from userapp.admin import alternative_site

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^alt-admin/', include(alternative_site.urls)),
    (r'^', include('userapp.urls')),
)
