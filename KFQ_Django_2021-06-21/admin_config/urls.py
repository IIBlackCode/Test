"""admin_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

import BRAND
import ERP
from BRAND import views
from ERP import views

urlpatterns = [
    path('',BRAND.views.theme_index),
    path('admin/', admin.site.urls),

    #Brand 관련 페이지
    # path('BRAND/', BRAND.views.index),
    path('BRAND/', include('BRAND.urls')),


    #ERP system 관련 페이지
    path('ERP/', include('ERP.urls')),
]
