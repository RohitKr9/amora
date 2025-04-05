from django.urls import path
from .views import loginView, signupView

urlpatterns = [
    path('login/', loginView, name = 'login'),
    path("signup/", signupView, name = 'signup'),
]
