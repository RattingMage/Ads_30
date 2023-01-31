from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsSelectionOwner(BasePermission):
    message = "You're not owner."

    def has_object_permission(self, request, view, selection):
        if request.user == selection.owner:
            return True
        return False


class IsAdOwnerOrAdmin(BasePermission):
    message = "You can't update it."

    def has_object_permission(self, request, view, ad):
        if request.user == ad.author or request.user.role != UserRoles.MEMBER:
            return True
        return False
