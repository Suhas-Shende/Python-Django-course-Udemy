from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsStudentOrAdminReadOnly(BasePermission):
    message="Only student who have their own account logged in can modify the data or Admin can modify the data"
    def has_permission(self, request, view):
        if request.user.is_student or request.user.is_staff:
            return True
        

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user==request.user
        