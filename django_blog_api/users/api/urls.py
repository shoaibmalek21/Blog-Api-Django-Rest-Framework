from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from users.api.views import (
	UserCreateAPIView,
	UserLoginAPIView,
	)

urlpatterns = [
	path('login/', UserLoginAPIView.as_view(), name='login'),
	path('register/', UserCreateAPIView.as_view(), name='register'),
]