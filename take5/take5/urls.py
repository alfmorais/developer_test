"""take5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from survey import (viewsets, serializers)


# to define general routes for API
route = routers.DefaultRouter()


# defined routes to SURVEY API
# Survey
route.register(r'survey', viewsets.SurveyQuestionAlternativeViewSet,
               basename="SurveyDetail")


urlpatterns = [
    path('admin/', admin.site.urls),
    # url standard from Django Rest Framework
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    # url for API
    path('', include(route.urls)),
]
