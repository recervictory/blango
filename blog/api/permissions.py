from rest_framework import permissions

<<<<<<< HEAD
class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)
=======
>>>>>>> a90382d38cd4db768ae2601129171384b40ef423

class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

<<<<<<< HEAD
        return request.user == obj.author
=======
        return request.user == obj.author

class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)
>>>>>>> a90382d38cd4db768ae2601129171384b40ef423
