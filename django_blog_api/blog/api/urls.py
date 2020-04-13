from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from blog.api.views import (
	PostListAPIView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	PostCreateAPIView,
	)

urlpatterns = [
	path('', PostListAPIView.as_view(), name='list'),
	path('create/', PostCreateAPIView.as_view(), name='create'),
    # path('/<int:pk>/', PostDetailView.as_view(), name='detail'),
	url(r'^(?P<title>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<title>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='edit'),
	url(r'^(?P<title>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),

]