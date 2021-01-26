import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,  password, **extra_fields):
        '''
        Create and return a `User` with superuser (admin) permisissions.
        '''
        if password is None:
            raise TypeError('Superusers must have a password.')
        user = self.create_user(email, password, is_superuser=True)
        user.is_staff = True
        user.is_superuser = True
        
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()


class Calendar(models.Model):
    pass


class Doctor(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   first_name = models.CharField(max_length=255) 
   last_name = models.CharField(max_length=255) 
   specialty = models.CharField(max_length=255) 
   availability = models.ForeignKey(Calendar, on_delete=models.CASCADE, null=True)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    date_of_birth = models.CharField(max_length=255) 
    address = models.CharField(max_length=255) 
   

class Appointment(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason_for_visit = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


