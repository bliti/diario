from django.conf.urls import patterns, url
from .views import CosaCreate, CosaDetail

urlpatterns = patterns('',
    # ...
    url(r'cosa/add/$', CosaCreate.as_view(), name='cosa-add'),
    url(r'^cosa/([\w-]+)/$', CosaDetail.as_view(), name='cosa-detail'),
    )