# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblUsers(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pword = models.CharField(db_column='PWord', max_length=300, blank=True, null=True)  # Field name made lowercase.
    textingphone = models.CharField(db_column='TextingPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    utype = models.IntegerField(db_column='UType', blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    activationcode = models.CharField(db_column='ActivationCode', max_length=6, blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    usermembership = models.IntegerField(db_column='UserMembership', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Users'
