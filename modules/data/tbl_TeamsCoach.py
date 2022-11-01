# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblTeamscoach(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('TblUsers', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeID')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=50)  # Field name made lowercase.
    coachname = models.CharField(db_column='CoachName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coachphone = models.CharField(db_column='CoachPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coachemail = models.CharField(db_column='CoachEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stateid = models.ForeignKey('TblStates', models.DO_NOTHING, db_column='StateID')  # Field name made lowercase.
    createdt = models.DateTimeField(db_column='CreateDT')  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='UpdateDT')  # Field name made lowercase.
    ranktype = models.IntegerField(db_column='RankType', blank=True, null=True)  # Field name made lowercase.
    mergedwith = models.IntegerField(db_column='MergedWith', blank=True, null=True)  # Field name made lowercase.
    yboa_id = models.IntegerField(db_column='YBOA_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_TeamsCoach'
