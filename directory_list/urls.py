from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^$', 'directory_list.views.filetree', name="list"),
)
