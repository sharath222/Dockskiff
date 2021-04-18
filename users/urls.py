from django.contrib import admin
from django.urls import path, include
from .views import UserLoginView, UserRegistrationView

#url patterns coming from docskiff folder urls.py users/
urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('signup/', UserRegistrationView.as_view())
]