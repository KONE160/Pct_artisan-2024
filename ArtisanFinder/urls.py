"""
URL configuration for ArtisanFinder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from . import views 
from django.conf import settings
from django.conf.urls.static import static

# from .views import inscription

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('artisan/', views.trouverArtisan_view, name='artisan'),
    path('connexion/', views.connexion_view, name='connexion'),
    path('espaceArtisan/', views.espaceArtisan_view, name='espace-artisan'),
    path('contact/', views.contact_view, name='contact'),
    path('apropos/', views.apropos_view, name= 'apropos'),
    path('cgu/',views.cgu_view, name= 'cgu'),
    path('cgv/', views.cgv_view, name= 'cgv'),
    path('mentions-legales/', views.mentions_view, name= 'mentions-legales'),
    path('vieprivee/', views.vieprivee_view, name= 'vieprivee'),
    path('equipe/', views.equipe_view, name = 'equipe'),
    path('inscription/',views.inscription_view, name='inscription'),
    path('register/', views.inscription, name='register'),
    path('password-oublie/', views.passwor_oublie_view, name='password-oublie'),
     
     ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

   