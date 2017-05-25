from django.conf.urls import url



from api import views


urlpatterns = [

    url(r'^$', views.api_root, name='api-root'),

    url(r'^authentication', views.authentication, name="authentication"),

    url(r'^image_upload/(?P<pk>[0-9]+)/$', views.FileUploadView.as_view(), name="image_upload"),

    url(r'^accounts/$', views.UserListApiView.as_view(), name="accounts-list"),
    url(r'^accounts/(?P<pk>\d+)/$', views.UserDetail.as_view(), name="user-detail"),

    url(r'^ratings/$', views.RatingList.as_view(), name="rating-list"),
    url(r'^ratings/(?P<pk>\d+)/$', views.RatingDetail.as_view(), name="rating-detail"),

    url(r'^spots/$', views.SpotList.as_view(), name="spot-list"),
    url(r'^spots/(?P<pk>\d+)/$', views.SpotDetail.as_view(), name="spot-detail"),

    url(r'^certificated_spots/$', views.CertificatedSpotList.as_view(), name="certificated-spot-list"),

    url(r'^favourites_spots/$', views.UserFavouritesSpotListApiView.as_view(), name="user-favourites-spot-list"),
    url(r'^favourites_spots/(?P<pk>\d+)/$', views.UserFavouritesSpotDetail.as_view(), name="usersspotslist-detail"),


    url(r'^nearby/(?P<lat>-?\d{2,3}.\d{5})/(?P<lng>-?\d{2,3}.\d{5})?/$', views.nearby_spots, name="nearby_spots"),
    url(r'^nearby/(?P<lat>-?\d{1,3}.\d{5})/(?P<lng>-?\d{1,3}.\d{5})/(?P<radius>\d*)$', views.nearby_spots, name="nearby_spots_with_radius"),
]
