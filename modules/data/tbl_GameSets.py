# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblGamesets(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID', blank=True, null=True)  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='DivisionID', blank=True, null=True)  # Field name made lowercase.
    poolid = models.IntegerField(db_column='PoolID', blank=True, null=True)  # Field name made lowercase.
    gameid = models.IntegerField(db_column='GameID', blank=True, null=True)  # Field name made lowercase.
    setnbr = models.IntegerField(db_column='SetNbr', blank=True, null=True)  # Field name made lowercase.
    homescore = models.IntegerField(db_column='HomeScore', blank=True, null=True)  # Field name made lowercase.
    visitorscore = models.IntegerField(db_column='VisitorScore', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_GameSets'
