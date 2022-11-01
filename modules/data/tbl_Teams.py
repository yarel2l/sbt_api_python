# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblTeams(models.Model):
    teamid = models.AutoField(db_column='TeamID', primary_key=True)  # Field name made lowercase.
    smsid = models.IntegerField(db_column='SMSID', blank=True, null=True)  # Field name made lowercase.
    teamtxtid = models.IntegerField(db_column='TeamTxtID', blank=True, null=True)  # Field name made lowercase.
    gradeid = models.IntegerField(db_column='GradeID', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coachname = models.CharField(db_column='CoachName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coachphone = models.CharField(db_column='CoachPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    coachemail = models.CharField(db_column='CoachEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    assistantname = models.CharField(db_column='AssistantName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    assistantphone = models.CharField(db_column='AssistantPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatetid = models.IntegerField(db_column='UpdateTID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Teams'
