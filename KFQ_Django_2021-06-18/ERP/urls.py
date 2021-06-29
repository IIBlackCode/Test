from django.urls import path

from ERP import views

urlpatterns = [
    path('test/', views.index),

#template link
    path('template/index/', views.template_index, name='index.html'),
]