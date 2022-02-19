from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from patients import views

urlpatterns = [
    # Path to access the admin page
    path('admin/', admin.site.urls),
    # Path to render the Homepage
    path('', views.frontend, name='frontend'),
    # Path Login/Logout
    path('login/', include('django.contrib.auth.urls')),

    # ===============
    # BACKEND SECTION
    # ===============
    # Path to access the backend page
    path('backend/', views.backend, name='backend'),
    # Path to add patient
    path('add_patient', views.add_patient, name='add_patient'),
    # Path to delete patient
    path('delete_patient/<str:patient_id>',
         views.delete_patient, name='delete_patient'),
    # Path to access the patient individually
    path('patient/<str:patient_id>',
         views.patient, name='patient'),
]
