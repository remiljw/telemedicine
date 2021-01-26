from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserLoginSerializer, PatientSignUpSerializer, AddDoctorSerializer
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
            return Response(serializers.data, response)
        else:
            return Response(serializer._errors, status=HTTP_400_BAD_REQUEST)

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
            return Response(response, status=status_code)
        else:
            return Response(serializer._errors, status=HTTP_400_BAD_REQUEST)



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