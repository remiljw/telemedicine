from datetime import datetime, date
from .utils import validate_dates
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsDoctor
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserLoginSerializer, PatientSignUpSerializer, AddDoctorSerializer, AppointmentSerializer, CalendarSerializer
from .models import Doctor,Patient, User, Appointment, Calendar
# Create your views here.







class PatientSignUpView(CreateAPIView):
    serializer_class = PatientSignUpSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
            'success' : 'True',
            'status code' : status_code,
            'message' : 'Patient registered successfully'
            }
            return Response(serializer.data, status=status_code)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class AddDoctorView(CreateAPIView):
    serializer_class = AddDoctorSerializer
    permission_classes = (IsAdminUser,)


    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            status_code = status.HTTP_201_CREATED
            response = {
            'success' : 'True',
            'status code' : status_code,
            'message' : 'Doctor added successfully'
            }
            return Response(serializer.data, status=status_code)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class UserLoginView(RetrieveAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        pass

    def get_object(self):
        pass

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

class CalendarView(CreateAPIView):
    serializer_class = CalendarSerializer
    permission_classes = (IsDoctor,)

    # @validate_dates
    def post(self, request):
        check_date = request.data['date']
        new_date = datetime.strptime(check_date, '%Y-%m-%d').date()
        today = date.today()
        if new_date < today:
            return Response('Date cannot be yesterday or before', status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user.doctor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
















class BookAppointmentView(CreateAPIView):
    serializer_class = AppointmentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(patient=request.user.patient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)