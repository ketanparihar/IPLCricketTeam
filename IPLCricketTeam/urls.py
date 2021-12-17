"""IPLCricketTeam URL Configuration

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
from IPLWebApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blist', views.BangloreViewset, basename='bangalore')

router = DefaultRouter()
router.register('clist', views.ChennaiViewset, basename='chennai')

router = DefaultRouter()
router.register('mlist', views.MumbaiViewset, basename='mumbai')

router = DefaultRouter()
router.register('plist', views.PunjabViewset, basename='punjab')

router = DefaultRouter()
router.register('rlist', views.RajasthanViewset, basename='rajasthan')

router = DefaultRouter()
router.register('klist', views.KolkataViewset, basename='kolkata')

router = DefaultRouter()
router.register('dlist', views.DelhiViewset, basename='delhi')

router = DefaultRouter()
router.register('hlist', views.HyderabadViewset, basename='hyderabad')


urlpatterns = [
    path('banglorelist/', include(router.urls)),
    path('chennailist/', include(router.urls)),
    path('mumbailist/', include(router.urls)),
    path('punjablist/', include(router.urls)),
    path('hyderabadlist/', include(router.urls)),
    path('kolkatalist/', include(router.urls)),
    path('delhilist/', include(router.urls)),
    path('punjablist/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('bangalore/', views.bangalore),
    path('detail/', views.detail),
    path('addplayers/', views.addPlayers),
    path('addteam/', views.addteam),
    path('thanks/', views.thanks),
    path('chennai/', views.Chennai),
    path('mumbai/', views.Mumbai),
    path('delhi/', views.Delhi),
    path('kolkata/', views.Kolkata),
    path('rajasthan/', views.Rajasthan),
    path('punjab/', views.Punjab),
    path('hyderabad/', views.Hyderabad),
    path('search/', views.SearchTeam, name='Search-Team')
]
