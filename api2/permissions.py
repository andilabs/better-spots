import operator

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `user` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        if hasattr(view, 'object_user_to_check'):
            object_user_to_check = operator.attrgetter(view.object_user_to_check)(obj)
        else:
            object_user_to_check = obj.user
        return object_user_to_check == request.user
