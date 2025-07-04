from rest_framework.permissions import BasePermission
from datetime import datetime


class IsEvenYear(BasePermission):
    message = "⛔ Faqat juft yillarda (2024, 2026, ...) kirish mumkin."

    def has_permission(self, request, view):
        return datetime.now().year % 2 == 0 or datetime.now().year == 2025


class IsSuperUserOnly(BasePermission):
    message = "⛔ Faqat superuserlar uchun ruxsat berilgan."

    def has_permission(self, request, view):
        return request.user.is_superuser


class OnlyPutPatchAllowed(BasePermission):
    message = "⛔ Faqat PUT yoki PATCH so'rovlariga ruxsat bor."

    def has_permission(self, request, view):
        return request.method in ['PUT', 'PATCH']