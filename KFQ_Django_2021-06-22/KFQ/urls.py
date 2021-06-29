from django.urls import path

from KFQ import views

urlpatterns = [
    path('2021-06-22/01/', views.Date2021_06_22.no_01, name='01_basic.html'),
    path('2021-06-22/02/', views.Date2021_06_22.no_02, name='02_operator.html'),
    path('2021-06-22/03/', views.Date2021_06_22.no_03, name='03_ajax.html'),
    path('2021-06-22/04/', views.Date2021_06_22.no_04, name='04.html'),
    path('2021-06-22/05/', views.Date2021_06_22.no_05, name='05.html'),
    path('2021-06-22/06/', views.Date2021_06_22.no_06, name='06.html'),
    path('2021-06-22/07/', views.Date2021_06_22.no_07, name='07.html'),
    # path('2021-06-22/01/', views.Date2021_06_22.no_01),
]