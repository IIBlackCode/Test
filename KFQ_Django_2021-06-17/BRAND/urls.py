from django.urls import path

from BRAND import views

urlpatterns = [
    path('test/', views.index),

    #template link
    path('template/index/', views.template_index, name='index.html'),

]