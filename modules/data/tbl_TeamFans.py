# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblTeamfans(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID')  # Field name made lowercase.
    smsid = models.IntegerField(db_column='SMSID', blank=True, null=True)  # Field name made lowercase.
    teamtxtid = models.IntegerField(db_column='TeamTxtID', blank=True, null=True)  # Field name made lowercase.
    teamid = models.IntegerField(db_column='TeamID')  # Field name made lowercase.
    teaminfoid = models.IntegerField(db_column='TeamInfoID', blank=True, null=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cellphone = models.CharField(db_column='CellPhone', max_length=11)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_TeamFans'
