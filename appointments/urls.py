from django.urls import path

from . import views

app_name = 'appointments'

urlpatterns = [
    path('patient-signup/', views.PatientSignUpView.as_view(), name='patient-signup'),
    path('signin/', views.UserLoginView.as_view(), name='signin'),
    path('add-doctor/', views.AddDoctorView.as_view(), name='add-doctor'),
    path('doc-calendar/', views.CalendarView.as_view(),  name='doc-calendar'),
    path('book-appointment/', views.BookAppointmentView.as_view(), name='book-appointment'),
]
