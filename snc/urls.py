from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('uhome/',views.uhome,name='uhome'),
    path('help/',views.help,name='help'),
    path('settings/',views.settings,name='settings'),
    path('ahome/',views.ahome,name='ahome'),
    path('shome/',views.shome,name='shome'),
    path('hcontactus/',views.hcontactus,name='hcontactus'),
    path('haboutus/',views.haboutus,name='haboutus'),
    path('hprivacypolicy/',views.hprivacypolicy,name='hprivacypolicy'),
    path('hterms/', views.hterms, name='hterms'),
    path('vuharley/', views.vuharley, name='vuharley'),
    path('atuser/', views.atuser, name='atuser'),
    path('atauction/', views.atauction, name='atauction'),
    path('alauction/', views.alauction, name='alauction'),
    path('buser1/', views.buser1, name='buser1'),
    path('adharley/',views.adharley,name='adharley'),
    path('adrolex1/', views.adrolex1, name='adrolex1'),
    path('adthar1/',views.adthar1,name='adthar1'),
    path('adlamborghini1/', views.adlamborghini1, name='adlamborghini1'),
    path('adwatch1/', views.adwatch1, name='watch1'),
    path('adguitar1/', views.adguitar1, name='adguitar1'),
    path('adrareart1/', views.adrareart1, name='adrareart1'),
    path('adsneaker1/', views.adsneaker1, name='adsneaker1'),
    path('adhermesh1/', views.adhermesh1, name='adhermesh1'),
    path('adhondarc30/', views.adhondarc30, name='adhondarc30'),
    path('adnecklace1/',views.adnecklace1,name='adnecklace'),
    path('addadmin/',views.addadmin,name='addadmin')
]