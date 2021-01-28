from rest_framework import permissions
# from.models import Doctor

class IsDoctor(permissions.BasePermission):

    message = 'Only Doctors can add date to calendar'
   

    def has_permission(self, request, view):
        user = request.user
        if user.is_anonymous:
            return False
        
        if user.is_doctor == True:
            return True
        else:
            self.message = ('Permission denied, user is not a doctor')
            return False
        # try:
        #     user.is_doctor = True
        # except Doctor.DoesNotExist:
        #     self.message = ("Permission denied, user is not a doctor")
        #     return False
        # return user == user.doctor