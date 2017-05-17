from django.conf.urls import include, url

from rest_framework.schemas import get_schema_view
from rest_framework_nested import routers
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from api2.spots.views import SpotViewSet
from api2.opinions.views import OpinionViewSet

router = routers.SimpleRouter()

router.register(r'spots', SpotViewSet)

spot_router = routers.NestedSimpleRouter(router, r'spots', lookup='spot')
spot_router.register(r'opinions', OpinionViewSet, base_name='opinions')


schema_view = get_schema_view(title='Spots API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer], public=True)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(spot_router.urls)),
    url('^schema/', schema_view),
]
