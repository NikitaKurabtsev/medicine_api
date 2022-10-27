from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only company owners or admin are able to edit their medicines.
    """
    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve'):
            return True

        return obj.company.owner == request.user
