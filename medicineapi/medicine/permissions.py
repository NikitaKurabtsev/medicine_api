from rest_framework import permissions

ACTION_SAFE_METHODS = [
    'list',
    'retrieve'
]


# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """Allow company owners to edit their medicines."""
    
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.company.owner == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Allow company owners to edit their medicines."""
    def has_object_permission(self, request, view, obj):
        if view.action in ACTION_SAFE_METHODS:
            return True

        return obj.company.owner == request.user
