from django.contrib import admin
from django.urls import path
from patients import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", views.frontend, name="frontend")
]
