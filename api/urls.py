from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns

from api import views


# place app url patterns here

urlpatterns = patterns(
    '',
    url(r'^image_upload/(?P<pk>[0-9]+)/$', views.FileUploadView.as_view(), name="image_upload"),

    url(r'^authentication', 'api.views.authentication', name="authentication"),

    url(r'^users/$', views.SpotUserList.as_view(), name="users-list"),
    url(r'^users/(?P<pk>\d+)/$', views.SpotUserDetail.as_view(), name="spotuser-detail"),

    url(r'^opinionusefulnessrating/(?P<pk>\d+)/$', views.OpinionUsefulness.as_view(), name="opinionusefulnessrating-detail"),
    url(r'^opinions/(?P<pk>\d+)/$', views.OpinionDetail.as_view(), name="opinion-detail"),

    url(r'^raitings/$', views.RaitingList.as_view(), name="raiting-list"),
    url(r'^raitings/(?P<pk>\d+)/$', views.RaitingDetail.as_view(), name="raiting-detail"),

    url(r'^spots/$', views.SpotList.as_view(), name="spot-list"),
    url(r'^spots/(?P<pk>\d+)/$', views.SpotDetail.as_view(), name="spot-detail"),

    url(r'^nearby/$', 'api.views.nearby_spots'),
    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})?/$', 'api.views.nearby_spots', name="nearby_spots"),
    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})/(?P<radius>\d*)$', 'api.views.nearby_spots'),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
