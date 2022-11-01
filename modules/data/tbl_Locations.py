# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblLocations(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='Zipcode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    director2 = models.CharField(db_column='Director2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cellphone2 = models.CharField(db_column='CellPhone2', max_length=48)  # Field name made lowercase.
    director3 = models.CharField(db_column='Director3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cellphone3 = models.CharField(db_column='CellPhone3', max_length=48)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    getscores = models.IntegerField(db_column='GetScores', blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Locations'
