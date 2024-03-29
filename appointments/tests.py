from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from datetime import date
from rest_framework.test import APITestCase
from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer
# Create your tests here.
User = get_user_model()



class AppointmentsAPITests(APITestCase):
    def test_patient_account(self):
        url = reverse('appointments:patient-signup')
        data = {
            'email': 'patient@test.com',
            'password': 'TestPatient@21',
            'patient':
                    {
                        'first_name': 'John',
                        'last_name': 'Doe',
                        'date_of_birth': '1986-05-25',
                        'address': '567, Lagos Road, Anthony.'
                    }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_admin(self):
        User.objects.create_superuser(
            email='test@admin.com', password='MasterPW200'
        )


    def test_admin_token(self):
        self.test_create_admin()
        url = reverse('appointments:signin')
        data = {
            'email' : 'test@admin.com',
            'password' : 'MasterPW200'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


    def test_doctor_account(self):
        url = reverse('appointments:add-doctor')
        data = {
            'email' : 'doctor@test.com',
            'password': 'TestDoctor@22',
            'doctor':
                {
                    'first_name': 'James',
                    'last_name': 'Doe',
                    'specialty' : 'Paediatrics'
                }
        }
        self.test_admin_token()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_doctor_token(self):
        self.test_doctor_account()
        url = reverse('appointments:signin')
        data = {
            'email' : 'doctor@test.com',
            'password': 'TestDoctor@22',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


    def test_patient_token(self):
        self.test_patient_account()
        url = reverse('appointments:signin')
        data = {
            'email': 'patient@test.com',
            'password': 'TestPatient@21'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('token' in response.data)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)


   
    def test_doc_calendar(self):
        url = reverse('appointments:doc-calendar')
        data = {
            'date' : date.today()
        }
        self.test_doctor_token()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   
    
    def test_appointment(self):
        self.test_doc_calendar()
        self.test_patient_token()
        url = reverse('appointments:book-appointment')
        data = {
            'doctor' : 1,
            'date' : 1,
            'time' : 2,
            'reason_for_visit': 'Sore Throat',
            
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
