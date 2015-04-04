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

        return obj.user == request.user


class IsAdmin(permissions.BasePermission):
    """Allow access for Admin only"""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated():
            return False
        if request.user.is_admin:
            return True

        return False
