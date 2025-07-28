



from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsAdminReadOnly(BasePermission):

    """Only Admin can modify the data"""

    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff