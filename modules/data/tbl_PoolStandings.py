# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblPoolstandings(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID')  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='DivisionID')  # Field name made lowercase.
    gamenbr = models.IntegerField(db_column='GameNbr', blank=True, null=True)  # Field name made lowercase.
    playoffpoolid = models.IntegerField(db_column='PlayoffPoolID', blank=True, null=True)  # Field name made lowercase.
    poolid = models.IntegerField(db_column='PoolID', blank=True, null=True)  # Field name made lowercase.
    poolname = models.CharField(db_column='PoolName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    teamid = models.IntegerField(db_column='TeamID', blank=True, null=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    win = models.IntegerField(db_column='Win', blank=True, null=True)  # Field name made lowercase.
    lost = models.IntegerField(db_column='Lost', blank=True, null=True)  # Field name made lowercase.
    setwin = models.IntegerField(db_column='SetWin', blank=True, null=True)  # Field name made lowercase.
    setlost = models.IntegerField(db_column='SetLost', blank=True, null=True)  # Field name made lowercase.
    setpct = models.FloatField(db_column='SetPCT', blank=True, null=True)  # Field name made lowercase.
    tie = models.IntegerField(db_column='Tie', blank=True, null=True)  # Field name made lowercase.
    pct = models.FloatField(db_column='PCT', blank=True, null=True)  # Field name made lowercase.
    h2h_wl = models.CharField(db_column='H2H_WL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    h2h = models.FloatField(db_column='H2H', blank=True, null=True)  # Field name made lowercase.
    pt = models.FloatField(db_column='PT', blank=True, null=True)  # Field name made lowercase.
    pointsall = models.IntegerField(db_column='PointsAll', blank=True, null=True)  # Field name made lowercase.
    pf = models.FloatField(db_column='PF', blank=True, null=True)  # Field name made lowercase.
    pa = models.FloatField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    credits = models.IntegerField(db_column='Credits', blank=True, null=True)  # Field name made lowercase.
    debits = models.IntegerField(db_column='Debits', blank=True, null=True)  # Field name made lowercase.
    pointstie2 = models.IntegerField(db_column='PointsTie2', blank=True, null=True)  # Field name made lowercase.
    coin = models.IntegerField(db_column='Coin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_PoolStandings'
