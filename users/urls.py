from django.urls import path
from . import views

urlpatterns = [
    # Other URLs...
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
]