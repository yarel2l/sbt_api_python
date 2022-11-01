# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblTournaments(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    eventtype = models.IntegerField(db_column='EventType', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactphone = models.CharField(db_column='ContactPhone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    getscores = models.IntegerField(db_column='GetScores', blank=True, null=True)  # Field name made lowercase.
    contactname2 = models.CharField(db_column='ContactName2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactphone2 = models.CharField(db_column='ContactPhone2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    intervals = models.IntegerField(db_column='Intervals', blank=True, null=True)  # Field name made lowercase.
    gameduration = models.IntegerField(db_column='GameDuration', blank=True, null=True)  # Field name made lowercase.
    organization = models.IntegerField(db_column='Organization', blank=True, null=True)  # Field name made lowercase.
    maxpoints = models.IntegerField(db_column='MaxPoints')  # Field name made lowercase.
    active = models.IntegerField(db_column='Active')  # Field name made lowercase.
    timezone = models.IntegerField(db_column='TimeZone', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)  # Field name made lowercase.
    bracketstyle = models.IntegerField(db_column='BracketStyle', blank=True, null=True)  # Field name made lowercase.
    smsid = models.IntegerField(db_column='SMSID', blank=True, null=True)  # Field name made lowercase.
    blocksms = models.IntegerField(db_column='BlockSMS', blank=True, null=True)  # Field name made lowercase.
    robot = models.IntegerField(db_column='ROBOT', blank=True, null=True)  # Field name made lowercase.
    divisiondesc = models.CharField(db_column='DivisionDesc', max_length=10, blank=True, null=True)  # Field name made lowercase.
    genderdesc = models.CharField(db_column='GenderDesc', max_length=10, blank=True, null=True)  # Field name made lowercase.
    multiregistrations = models.IntegerField(db_column='MultiRegistrations', blank=True, null=True)  # Field name made lowercase.
    lastrelease = models.DateTimeField(db_column='LastRelease', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)  # Field name made lowercase.
    registrationpriceperteam = models.DecimalField(db_column='RegistrationPricePerTeam', max_digits=6, decimal_places=2)  # Field name made lowercase.
    registrationfee = models.DecimalField(db_column='RegistrationFee', max_digits=6, decimal_places=2)  # Field name made lowercase.
    registrationstartdate = models.DateTimeField(db_column='RegistrationStartDate')  # Field name made lowercase.
    registrationenddate = models.DateTimeField(db_column='RegistrationEndDate')  # Field name made lowercase.
    registrationcountteams = models.IntegerField(db_column='RegistrationCountTeams')  # Field name made lowercase.
    registrationdiscount = models.DecimalField(db_column='RegistrationDiscount', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Tournaments'
