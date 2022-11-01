# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblSmsphones(models.Model):
    smsid = models.AutoField(db_column='SMSID', primary_key=True)  # Field name made lowercase.
    smsphoneid = models.IntegerField(db_column='SMSPhoneID', blank=True, null=True)  # Field name made lowercase.
    smsphone = models.CharField(db_column='SMSPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descrip = models.CharField(db_column='Descrip', max_length=200, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    effectiveyear = models.IntegerField(db_column='EffectiveYear', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('TblOrganization', models.DO_NOTHING, db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_SMSPhones'
