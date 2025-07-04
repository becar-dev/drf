from rest_framework.permissions import BasePermission

from course.permission import *


class CompositePermission(BasePermission):


    """
    Barcha kerakli permissionlar bir joyda. Ulardan birortasi o'tmasa,
    mos ravishda message ko'rsatiladi.
    """
    message = "⛔ Ruxsat berilmagan."

    def __init__(self):
        self.permissions = [
            IsEvenYear(),
            IsSuperUserOnly(),
            OnlyPutPatchAllowed(),
        ]

    def has_permission(self, request, view):
        for perm in self.permissions:
            if not perm.has_permission(request, view):
                # Birinchi o‘tmagan permissiondan message olamiz
                self.message = getattr(perm, 'message', self.message)
                return False
        return True