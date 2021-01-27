from rest_framework import serializers
from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model, authenticate
from .models import Appointment, Doctor, Patient, Calendar
from rest_framework_jwt.settings import api_settings

User = get_user_model()

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name', 'specialty')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'date_of_birth', 'address')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

class PatientSignUpSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'patient')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        user = User.objects.create_user(**validated_data)
        Patient.objects.create(
            user = user,
            first_name = patient_data['first_name'],
            last_name = patient_data['last_name'], 
            date_of_birth = patient_data['date_of_birth'],
            address = patient_data['address'],
        )
        return user

class AddDoctorSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'doctor')
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        doctor_data = validated_data.pop('doctor')
        user = User.objects.create_user(**validated_data)
        Doctor.objects.create(
            user = user,
            first_name = doctor_data['first_name'],
            last_name = doctor_data['last_name'], 
            specialty = doctor_data['specialty'],
        )
        return user



class UserLoginSerializer(serializers.Serializer):


    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }
class CalendarSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    class Meta:
        model = Calendar
        fields = ('__all__')


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(slug_field='first_name', read_only=True)
    # patient = UserSerializer(many=False, read_only=True)
    # date = serializers.SlugRelatedField(slug_field='date', read_only=True)
    class Meta:
        model = Appointment
        fields = ('__all__')


