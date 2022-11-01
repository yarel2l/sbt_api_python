# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblTeampoints(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    teamid = models.IntegerField(db_column='TeamID', blank=True, null=True)  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID', blank=True, null=True)  # Field name made lowercase.
    gameid = models.IntegerField(db_column='GameID', blank=True, null=True)  # Field name made lowercase.
    pointsearned = models.IntegerField(db_column='PointsEarned', blank=True, null=True)  # Field name made lowercase.
    games = models.IntegerField(db_column='Games', blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField(db_column='Wins', blank=True, null=True)  # Field name made lowercase.
    isadded = models.BooleanField(db_column='IsAdded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_TeamPoints'
