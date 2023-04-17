from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsAdminOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
