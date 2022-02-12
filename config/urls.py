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
    path('add_patient', views.add_patient, name='add_patient')
]
