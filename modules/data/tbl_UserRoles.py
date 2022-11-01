# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblUserroles(models.Model):
    rollid = models.AutoField(db_column='RollID')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    moduleid = models.IntegerField(db_column='ModuleID', blank=True, null=True)  # Field name made lowercase.
    access = models.CharField(db_column='Access', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_UserRoles'
