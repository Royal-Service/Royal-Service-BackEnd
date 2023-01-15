from rest_framework import permissions
from django.http import QueryDict

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if obj is None:
            return True
        return obj.user == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        # hover over SAFE_METHODS to see which qualify
        if request.method in permissions.SAFE_METHODS:
            return True
        # if we're allowing the purchaser to be null in Model
        # then this will check for that case and allow access
        if obj.user is None:
            return True
        return obj.user.id == request.data['user']

class IsOpenOrClosed(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.status == True