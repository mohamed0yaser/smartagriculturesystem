from django.urls import path
from .views import MyTokenObtainPairView,UserDetailAPI,RegisterUserAPIView,ChangePasswordView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [    
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/get-details",UserDetailAPI.as_view()),
    path('api/register/',RegisterUserAPIView.as_view()),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),

]