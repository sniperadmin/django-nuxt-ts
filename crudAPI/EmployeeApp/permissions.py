from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, if obj is same with request.
        if request.method == 'GET' and obj == request.user:
          print(obj)
          print(request.user)
          return True
