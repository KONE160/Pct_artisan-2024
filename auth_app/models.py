from django.db import models

# Create your models here.

class Artisan(models.Model) :
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=100)
    Tel = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    DomaineActivite = models.CharField(max_length=100)
    AnneeExperience = models.IntegerField()
    Ville = models.CharField(max_length=70)
    MotDePasse = models.CharField(max_length=50)