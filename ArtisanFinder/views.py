from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def accueil_view(request) :
   return render(request, 'accueil.html')



def trouverArtisan_view(request) :
   return render(request, 'trouver_Artisan.html')


def services_view(request) : 
   return render(request,'services.html')

def contact_view(request):
   return render(request,'contact.html')

def espaceArtisan_view(request):
   return render(request,'espace_artisan.html')

def connexion_view(request):
   return render(request,'connexion.html')

def apropos_view(request):
   return render(request,'apropos.html')

def mentions_view(request):
   return render(request,'mentions.html')

def cgu_view(request):
   return render(request,'cgu.html')

def cgv_view(request):
   return render(request,'cgv.html')

def vieprivee_view(request):
   return render(request,'vieprivee.html')

def equipe_view(request):
   return render(request,'equipe.html')

