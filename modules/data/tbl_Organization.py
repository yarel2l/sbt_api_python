# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblOrganization(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    shortname = models.CharField(db_column='ShortName', max_length=15)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    director = models.IntegerField(db_column='Director', blank=True, null=True)  # Field name made lowercase.
    createdt = models.DateTimeField(db_column='CreateDT', blank=True, null=True)  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='UpdateDT', blank=True, null=True)  # Field name made lowercase.
    tiebreakingurl = models.TextField(db_column='TieBreakingURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Organization'
