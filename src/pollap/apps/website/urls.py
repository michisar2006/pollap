from django.urls import path
from .views import signup, UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name="signup"),
    
]
