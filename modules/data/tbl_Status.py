# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblStatus(models.Model):
    statusid = models.AutoField(db_column='StatusID', primary_key=True)  # Field name made lowercase.
    statusdesc = models.CharField(db_column='StatusDesc', max_length=50, blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='Details', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ranking = models.IntegerField(db_column='Ranking', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Status'
