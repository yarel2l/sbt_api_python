# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblDivisions(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    teamsperpool = models.IntegerField(db_column='TeamsPerPool', blank=True, null=True)  # Field name made lowercase.
    perpooldesc = models.CharField(db_column='PerPoolDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gamesperpool = models.IntegerField(db_column='GamesPerPool', blank=True, null=True)  # Field name made lowercase.
    gppdesc = models.CharField(db_column='GPPDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    brackets = models.IntegerField(db_column='Brackets', blank=True, null=True)  # Field name made lowercase.
    bracketsdesc = models.CharField(db_column='BracketsDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    minimumgames = models.IntegerField(db_column='MinimumGames', blank=True, null=True)  # Field name made lowercase.
    divisiontype = models.CharField(db_column='DivisionType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeID', blank=True, null=True)  # Field name made lowercase.
    sporttype = models.IntegerField(db_column='SportType', blank=True, null=True)  # Field name made lowercase.
    hideschedule = models.IntegerField(db_column='HideSchedule', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    maincolor = models.CharField(db_column='MainColor', max_length=7, blank=True, null=True)  # Field name made lowercase.
    altcolor = models.CharField(db_column='AltColor', max_length=7, blank=True, null=True)  # Field name made lowercase.
    hometextcolor = models.CharField(db_column='HomeTextColor', max_length=7, blank=True, null=True)  # Field name made lowercase.
    visitortextcolor = models.CharField(db_column='VisitorTextColor', max_length=7, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Divisions'
