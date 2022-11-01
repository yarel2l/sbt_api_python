# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblRefereeslots(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    refereeid = models.IntegerField(db_column='RefereeID')  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID')  # Field name made lowercase.
    slotid = models.IntegerField(db_column='SlotID', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    slotdate = models.DateField(db_column='SlotDate', blank=True, null=True)  # Field name made lowercase.
    timeid = models.IntegerField(db_column='TimeID', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_RefereeSlots'
