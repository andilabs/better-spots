from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from api2.accounts.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
