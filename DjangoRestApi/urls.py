"""DjangoRestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from DjangoRestApp import views
from rest_framework.authtoken import views as views2
router=routers.DefaultRouter()

router.register(r'posts',views.PostViewSets)
router.register(r'posts_2',views.PostViewSetsAlternate,basename="post_2")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/auth/token',TokenObtainPairView.as_view(),name="auth_token"),
    path('api/auth/refresh',TokenRefreshView.as_view(),name="auth_refresh_token"),
    path('token_generate/',views2.obtain_auth_token)
]
