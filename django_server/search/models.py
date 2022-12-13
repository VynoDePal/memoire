from django.db import models

# Create your models here.

class Archive(models.Model):
    id_archive = models.AutoField(db_column='ID Archive', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_archive = models.CharField(db_column='Code Archive', max_length=8)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    intitulé_archive = models.CharField(db_column='Intitulé Archive', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_creation = models.DateTimeField(auto_now_add=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_archivage = models.DateTimeField(auto_now=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    durée_de_vie = models.DateField(db_column='Durée de vie')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fichier = models.FileField(upload_to='archives/')  # Field name made lowercase.
    nature = models.CharField(db_column='Nature', max_length=255)  # Field name made lowercase.
    # service = models.ForeignKey('Service', on_delete=models.CASCADE)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # secteur = models.ForeignKey('SecteurDActivit', on_delete=models.CASCADE)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    # auth_user = models.ManyToManyField('Auth_user', related_name='archives', blank=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'archives'

    def __str__(self):
        return self.intitulé_archive

    #def get_absolute_url(self):
        #return reversed('model-detail-view', args=[str(self.id_archive)])


class SecteurDActivit(models.Model):
    id_secteur = models.AutoField(db_column='ID Secteur', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_secteur = models.CharField(db_column='Code Secteur', max_length=8)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom_secteur = models.CharField(db_column='Nom Secteur', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_secteur = models.CharField(db_column='Type Secteur', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "secteur d'activité"

    def __str__(self):
        return self.nom_secteur

    #def get_absolute_url(self):
        #return reversed('model-detail-view', args=[str(self.id_secteur)])

class Service(models.Model):
    id_servive = models.AutoField(db_column='ID Servive', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_service = models.CharField(db_column='Code Service', max_length=8)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom_service = models.CharField(db_column='Nom Service', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'services'

    def __str__(self):
        return self.nom_service

    #def get_absolute_url(self):
        #return reversed('model-detail-view', args=[str(self.id_servive)])