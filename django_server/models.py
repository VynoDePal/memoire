# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Archives(models.Model):
    id_archive = models.AutoField(db_column='ID Archive', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_archive = models.CharField(db_column='Code Archive', max_length=8)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    intitulΘ_archive = models.CharField(db_column='IntitulΘ Archive', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_crΘation = models.DateTimeField(db_column='Date CrΘation')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_archivage = models.DateTimeField(db_column='Date Archivage')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    durΘe_de_vie = models.DateField(db_column='DurΘe de vie')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fichier = models.CharField(db_column='Fichier', max_length=255)  # Field name made lowercase.
    nature = models.TextField(db_column='Nature')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'archives'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SecteurDActivit(models.Model):
    id_secteur = models.AutoField(db_column='ID Secteur', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_secteur = models.CharField(db_column='Code Secteur', max_length=8)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom_secteur = models.CharField(db_column='Nom Secteur', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_secteur = models.CharField(db_column='Type Secteur', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = "secteur d'activitΘ"


class Services(models.Model):
    id_servive = models.AutoField(db_column='ID Servive', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    code_service = models.CharField(db_column='Code Service', max_length=8)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom_service = models.CharField(db_column='Nom Service', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'services'
