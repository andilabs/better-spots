try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# place app url patterns here
urlpatterns = patterns(
    '',
    url(r'^authentication', 'api.views.authentication'),
    # url(r'^foto/(?P<pk>\d+)/$', views.OtoFotoDetail.as_view(), name="otofoto-detail"),
    # url(r'^foto/$', views.OtoFotoList.as_view(), name="otofoto-list"),
    url(r'^users/$', views.SpotUserList.as_view(), name="users-list"),
    url(r'^users/(?P<pk>\d+)/$', views.SpotUserDetail.as_view(), name="dogspotuser-detail"),
    url(r'^opinionusefulnessrating/(?P<pk>\d+)/$', views.OpinionUsefulness.as_view(), name="opinionusefulnessrating-detail"),
    url(r'^opinions/(?P<pk>\d+)/$', views.OpinionDetail.as_view(), name="opinion-detail"),

    url(r'^raitings/$', views.RaitingList.as_view(), name="raiting-list"),
    url(r'^raitings/(?P<pk>\d+)/$', views.RaitingDetail.as_view(), name="raiting-detail"),
    url(r'^spots/$', views.SpotList.as_view(), name="spot-list"),
    url(r'^spots/(?P<pk>\d+)/$', views.SpotDetail.as_view(), name="spot-detail"),

    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})?/$', 'api.views.nearby_spots'),
    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})/(?P<radius>\d*)$', 'api.views.nearby_spots'),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])