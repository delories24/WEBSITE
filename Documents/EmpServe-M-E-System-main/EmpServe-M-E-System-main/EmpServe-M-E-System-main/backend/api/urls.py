from django.urls import path
from .views import UserRegistrationView
from .views import HomePageView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('register/', UserRegistrationView.as_view(), name='user-create'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('protected/', ProtectedView.as_view(), name='protected'),
]
