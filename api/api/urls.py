"""SOSPet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from argparse import Namespace
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from clinica.api.viewset import ClinicViewSet
from home.api.viewset import ContactViewSet, QuemSomosViewSet, RecipientViewSet
from ong.api.viewset import OngViewSet
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers
from animal.api.viewset import BreedViewSet, CoatViewSet, ColorViewSet, InterestViewSet, PetViewSet, PetSelViewSet, SpecieViewSet
from banner.api.viewset import BannerViewSet
from login.api.viewset import AddressViewSet, DocumentViewSet, LoginViewSet, TelephoneViewSet

router = routers.DefaultRouter()

router.register(r'v1/animal/pets', PetViewSet)
router.register(r'v2/animal/pets', PetSelViewSet)
router.register(r'v1/animal/species', SpecieViewSet)
router.register(r'v1/animal/breeds', BreedViewSet)
router.register(r'v1/animal/colors', ColorViewSet)
router.register(r'v1/animal/interests', InterestViewSet)
router.register(r'v1/animal/coats', CoatViewSet)
router.register(r'v1/login/address', AddressViewSet)
router.register(r'v1/login/documents', DocumentViewSet)
router.register(r'v1/login/users', LoginViewSet)
router.register(r'v1/login/phones', TelephoneViewSet)
router.register(r'v1/banner', BannerViewSet)
router.register(r'v1/clinic', ClinicViewSet)
router.register(r'v1/home/who-we-are', QuemSomosViewSet)
router.register(r'v1/home/contact', ContactViewSet)
router.register(r'v1/home/recipient', RecipientViewSet)
router.register(r'v1/ong', OngViewSet)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/auth', obtain_jwt_token),
    path('api/v1/refresh', refresh_jwt_token),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/api', permanent=False), name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)