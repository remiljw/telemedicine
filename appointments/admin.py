from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Patient, Doctor, Appointment, Calendar


# Register your models here.

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Calendar)


admin.site.unregister(Group)