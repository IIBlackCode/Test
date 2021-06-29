from django.urls import path

from KFQ import views

urlpatterns = [
    path('', views.no, name='contents.html'),

    path('2021-06-22/01/', views.Date2021_06_22.no_01, name='01_basic.html'),
    path('2021-06-22/02/', views.Date2021_06_22.no_02, name='02_operator.html'),
    path('2021-06-22/03/', views.Date2021_06_22.no_03, name='03_ajax.html'),
    path('2021-06-22/04/', views.Date2021_06_22.no_04, name='04.html'),
    path('2021-06-22/05/', views.Date2021_06_22.no_05, name='05.html'),
    path('2021-06-22/06/', views.Date2021_06_22.no_06, name='06.html'),
    path('2021-06-22/07/', views.Date2021_06_22.no_07, name='07.html'),
    # path('2021-06-22/01/', views.Date2021_06_22.no_01),

    path('2021-06-23/01/', views.Date2021_06_23.no_01, name='01.html'),
    path('2021-06-23/02/', views.Date2021_06_23.no_02, name='02.html'),
    path('2021-06-23/03/', views.Date2021_06_23.no_03, name='03.html'),
    path('2021-06-23/04/', views.Date2021_06_23.no_04, name='04.html'),
    path('2021-06-23/05/', views.Date2021_06_23.no_05, name='05.html'),
    path('2021-06-23/06/', views.Date2021_06_23.no_06, name='06.html'),
    path('2021-06-23/07/', views.Date2021_06_23.no_07, name='07.html'),
    path('2021-06-23/08/', views.Date2021_06_23.no_08, name='08.html'),
    path('2021-06-23/09/', views.Date2021_06_23.no_09, name='09.html'),
    path('2021-06-23/10/', views.Date2021_06_23.no_10, name='10.html'),
    path('2021-06-23/11/', views.Date2021_06_23.no_11, name='11.html'),
    path('2021-06-23/12/', views.Date2021_06_23.no_12, name='12.html'),
    path('2021-06-23/13/', views.Date2021_06_23.no_13, name='13.html'),
    path('2021-06-23/14/', views.Date2021_06_23.no_13, name='14.html'),
    path('2021-06-23/15/', views.Date2021_06_23.no_13, name='15.html'),
    path('2021-06-23/16/', views.Date2021_06_23.no_13, name='16.html'),
    path('2021-06-23/17/', views.Date2021_06_23.no_13, name='17.html'),
    path('2021-06-23/18/', views.Date2021_06_23.no_13, name='18.html'),

]