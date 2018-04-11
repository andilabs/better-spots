from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView


from www import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="www/mission.html"), name='main'),
    url(r'^certificated/$', views.CertificatedSpotListView.as_view(), name='certificated_list'),
    url(r'^certificated/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', views.CertificatedSpotDetailView.as_view(), name='certificated_detail'),
    url(r'^favourites/$', views.FavouritesSpotListView.as_view(), name='favourites_list'),
    url(r'^map/$', views.MapView.as_view(), name='map'),
    url(r'^mobile/', TemplateView.as_view(template_name="www/mobile.html"), name='mobile'),
    path('pdf/<int:pk>/', views.PDFStickerView.as_view(), name='pdf_sticker'),
    path('qrcode_link/<int:pk>/', views.QRCodeLinkView.as_view(), name='qrencode_link'),
    path('qrcode_link/<int:pk>/<int:size>/', views.QRCodeLinkView.as_view(), name='qrencode_link'),
    path('qrcode_vcard/<int:pk>/', views.QRCodeVCardView.as_view(), name='qrcode_vcard'),
    path('qrcode_vcard/<int:pk>/<int:size>/', views.QRCodeVCardView.as_view(), name='qrcode_vcard'),
    url(r'^spots/$', views.SpotListView.as_view(), name='spots_list'),
    url(r'^spots/add/', views.SpotCreateView.as_view(), name='add_spot'),
    url(r'^spots/(?P<pk>\d+)(?:/(?P<slug>[\w\d-]+))?/$', views.SpotDetailView.as_view(), name='spot'),
    path('vcard/<int:pk>/', views.VCardDownloadView.as_view(), name='vcard'),
]
