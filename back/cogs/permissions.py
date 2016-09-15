from rest_framework import permissions

class CogmakerOrReadOnly(permissions.BasePermission):
    """
    Custom permission so only Cog Maker users can make cogs,
    and only the creator can edit/delete cogs.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return request.user.user_type == 'cogmaker'
        else:
            return request.user == obj.owner


class SameTypeOnly(permissions.BasePermission):
    """
    Custom permission for same type user only notes.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.user_type == obj.owner.user_type:
            if request.method in permissions.SAFE_METHODS:
                return True
            return request.user == obj.owner


class OwnerOnly(permissions.BasePermission):
    """
    Custom permission for personal notes.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
