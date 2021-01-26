from django.urls import path

from . import views

app_name = 'appointments'

urlpatterns = [
    path('patient-signup/', views.PatientSignUpView.as_view()),
    path('signin/', views.UserLoginView.as_view()),
    path("add-doctor/", views.AddDoctorView.as_view()),
    # path("pending", views.get_all_pending_leaves),
    # path("accept/<int:pk>", views.leave_accept),
    # path("accepted", views.get_all_accepted_leaves),
]
