from django.conf.urls import url, patterns

from rest_framework.urlpatterns import format_suffix_patterns

from api import views


urlpatterns = patterns(
    '',

    # url(r'^$', views.api_root, name='api-root'),


    url(r'^authentication',
        views.authentication,
        name="authentication"),

    url(r'^image_upload/(?P<pk>[0-9]+)/$',
        views.FileUploadView.as_view(),
        name="image_upload"),

    url(r'^users/$',
        views.SpotUserList.as_view(),
        name="users-list"),
    url(r'^users/(?P<pk>\d+)/$',
        views.SpotUserDetail.as_view(),
        name="spotuser-detail"),

    url(r'^ratings/$',
        views.RatingList.as_view(),
        name="rating-list"),
    url(r'^ratings/(?P<pk>\d+)/$',
        views.RatingDetail.as_view(),
        name="rating-detail"),

    url(r'^spots/$',
        views.SpotList.as_view(),
        name="spot-list"),
    url(r'^spots/(?P<pk>\d+)/$',
        views.SpotDetail.as_view(),
        name="spot-detail"),

    url(r'^certificated_spots/$',
        views.CertificatedSpotList.as_view(),
        name="certificated-spot-list"),

    url(r'^favourites_spots/$',
        views.UserFavouritesSpotsList.as_view(),
        name="user-favourites-spot-list"),
    url(r'^favourites_spots/(?P<pk>\d+)/$',
        views.UserFavouritesSpotDetail.as_view(),
        name="usersspotslist-detail"),


    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})?/$',
        views.nearby_spots,
        name="nearby_spots"),
    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})/(?P<radius>\d*)$',
        views.nearby_spots,
        name="nearby_spots_with_radius"),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
