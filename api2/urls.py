from django.conf import settings
from django.conf.urls import include, url

from rest_framework.schemas import get_schema_view
from rest_framework_nested import routers
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from api2.accounts.views import UserViewSet
from api2.opinions.views import OpinionViewSet, UserOpinionViewSet
from api2.spots.views import SpotViewSet
from api2.ratings.views import RatingViewSet, UserRatingViewSet

router = routers.SimpleRouter()

router.register(r'spots', SpotViewSet)

spot_router = routers.NestedSimpleRouter(router, r'spots', lookup='spot')
spot_router.register(r'rates', RatingViewSet, base_name='rates')

rating_router = routers.NestedSimpleRouter(spot_router, r'rates', lookup='rate')
rating_router.register(r'opinion', OpinionViewSet, base_name='opinion')

router.register(r'users', UserViewSet)

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'rates', UserRatingViewSet, base_name='rates')

user_rating_router = routers.NestedSimpleRouter(user_router, r'rates', lookup='rate')
user_rating_router.register(r'opinion', UserOpinionViewSet, base_name='opinion')

schema_view = get_schema_view(
    title='{} API'.format(settings.SPOT_PROJECT_NAME),
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer],
    public=True)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(spot_router.urls)),
    url(r'^', include(rating_router.urls)),
    url(r'^', include(user_router.urls)),
    url('^schema/', schema_view),
]
