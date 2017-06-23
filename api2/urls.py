from django.conf import settings
from django.conf.urls import include, url

from rest_framework.schemas import get_schema_view
from rest_framework_nested import routers
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from api2.accounts.views import UserViewSet, UserFavouritesSpotsViewSet
from api2.opinions.views import OpinionViewSet, UserOpinionViewSet
from api2.spots.views import SpotViewSet
from api2.ratings.views import SpotsRatingViewSet, UserRatingViewSet

router = routers.SimpleRouter()

# spots/
router.register(r'spots', SpotViewSet)
spot_router = routers.NestedSimpleRouter(router, r'spots', lookup='spot')

# spots/<spot_pk>/rates/
spot_router.register(r'rates', SpotsRatingViewSet, base_name='spot-rates')

# spots/<spot_pk>/rates/<rate_pk>/
rating_router = routers.NestedSimpleRouter(spot_router, r'rates', lookup='rate')

# spots/<spot_pk>/rates/<rate_pk>/opinion/
rating_router.register(r'opinion', OpinionViewSet, base_name='spot-rate-opinion')


# users/
router.register(r'users', UserViewSet)
user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')

# users/<user_pk>/rates/
user_router.register(r'rates', UserRatingViewSet, base_name='user-rates')

# users/<spot_pk>/rates/<rate_pk>/
user_rating_router = routers.NestedSimpleRouter(user_router, r'rates', lookup='rate')

# users/<spot_pk>/rates/<rate_pk>/opinion/
user_rating_router.register(r'opinion', UserOpinionViewSet, base_name='user-rate-opinion')

# users/<user_pk>/favourites/
user_router.register('favourites', UserFavouritesSpotsViewSet, base_name='user-favourites')
user_favourites_router = routers.NestedSimpleRouter(user_router, 'favourites', lookup='spot')


schema_view = get_schema_view(
    title='{} API'.format(settings.SPOT_PROJECT_NAME),
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer],
    public=True
)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(spot_router.urls)),
    url(r'^', include(rating_router.urls)),
    url(r'^', include(user_router.urls)),
    url(r'^', include(user_rating_router.urls)),
    url(r'^', include(user_favourites_router.urls)),
    url('^schema/', schema_view),
]
