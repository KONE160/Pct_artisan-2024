# Generated by Django 5.0.6 on 2024-07-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtisanFinder', '0003_rename_metier_user_domaine_activite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscriptionclient',
            name='confirmer_le_mot_de_passe',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='inscriptionclient',
            name='mot_de_passe',
            field=models.CharField(max_length=60, null=True),
        ),
    ]