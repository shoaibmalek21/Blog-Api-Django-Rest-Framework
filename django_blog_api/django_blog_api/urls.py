"""django_blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),	
    path('login/', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'password_reset_done.html'), name='password_reset_done'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'password_reset_confirm.html'), name='password_reset_confirm'),
    path('', include('blog.urls')),
    url(r'^api/auth/token/', obtain_jwt_token),
    url(r'^api/posts/', include(('blog.api.urls','posts-api'), namespace='posts-api')),
    url(r'^api/users/', include(('users.api.urls','users-api'), namespace='users-api')),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
