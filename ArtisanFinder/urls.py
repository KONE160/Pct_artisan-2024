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
from django.contrib.auth import authenticate, login
from .forms import LoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('artisan/', views.trouverArtisan_view, name='artisan'),
    path('connexion/', views.login_view, name='login'),
    path('espaceArtisan/', views.espaceArtisan_view, name='espace-artisan'),
    path('contact/', views.contact_view, name='contact'),
    path('apropos/', views.apropos_view, name= 'apropos'),
    path('cgu/',views.cgu_view, name= 'cgu'),
    path('cgv/', views.cgv_view, name= 'cgv'),
    path('mentions-legales/', views.mentions_view, name= 'mentions-legales'),
    path('vieprivee/', views.vieprivee_view, name= 'vieprivee'),
    path('equipe/', views.equipe_view, name = 'equipe'),
    path('inscription/',views.inscription_view, name='inscription'),
    path('register/', views.profile_view, name='register'),
    path('password-oublie/', views.passwor_oublie_view, name='password-oublie'),
    path('choix/', views.choix_view, name= 'choix-inscription'),
    path('clientRegistration/', views.inscription_client_view, name= 'client-inscription'),
    path('profil/<int:artisan_id>/', views.profile_view, name='profil'),
    path('artisan/<int:artisan_id>/edit/', views.edit_profile_view, name='edit_profile_view'),
    path('artisan/change-password/', views.change_password_view, name='change_password_view'),
    path('artisan/<int:artisan_id>/add-portfolio-photo/', views.add_portfolio_photo_view, name='add_portfolio_photo_view'),
    # path('profil/', views.profil_view, name='profil'),
    
     
    
     ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

   