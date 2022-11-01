# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblInfoletter(models.Model):
    letterid = models.AutoField(db_column='LetterID')  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID')  # Field name made lowercase.
    letter = models.TextField(db_column='Letter', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flyerurl = models.CharField(db_column='FlyerURL', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_InfoLetter'
