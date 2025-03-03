from rest_framework.permissions import BasePermission, SAFE_METHODS

from apps.feedback.models import Comment

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request in SAFE_METHODS:
            return True
                
        return request.user.is_authenticated and (request.user == obj.owner)



    
class IsFeedbackOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'POST':
            return request.user.is_authenticated
        try:
            return request.user.is_authenticated and request.user == Comment.objects.get(id=view.kwargs['pk']).owner
        except:
            return 'Something went wrong'


