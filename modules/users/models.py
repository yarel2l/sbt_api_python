from django.conf import settings
from django.db import models


class ScorbotUser(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)
    username = models.CharField(db_column='UserName', max_length=50, unique=True)
    pword = models.CharField(db_column='PWord', max_length=300, blank=True, null=True)
    textingphone = models.CharField(db_column='TextingPhone', max_length=50, blank=True, null=True)
    utype = models.IntegerField(db_column='UType', blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)
    activationcode = models.CharField(db_column='ActivationCode', max_length=6, blank=True, null=True)
    active = models.BooleanField(db_column='Active', blank=True, null=True)
    email = models.TextField(db_column='Email', blank=True, null=True)
    usermembership = models.ForeignKey('Membership', on_delete=models.SET_NULL, db_column='UserMembership', blank=True, null=True)
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Users'


class UserRole(models.Model):
    rollid = models.AutoField(db_column='RollID', primary_key=True)
    userid = models.ForeignKey(ScorbotUser, db_column='UserID', on_delete=models.SET_NULL, blank=True, null=True)
    moduleid = models.ForeignKey('core.ScorbotModule', on_delete=models.SET_NULL, db_column='ModuleID', blank=True, null=True)
    access = models.CharField(db_column='Access', max_length=50, blank=True, null=True)
    accesscode = models.IntegerField(db_column='AccessCode', blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_UserRoles'


class Membership(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=255, blank=True, null=True)
    active = models.BooleanField(db_column='Active')

    class Meta:
        managed = False
        db_table = 'tbl_UsersMembership'


