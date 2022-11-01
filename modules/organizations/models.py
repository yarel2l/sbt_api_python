from django.db import models


class ScorbotOrganization(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    shortname = models.CharField(db_column='ShortName', max_length=15)
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)
    state = models.ForeignKey('states.ScorbotState', on_delete=models.SET_NULL, db_column='State', blank=True, null=True)
    contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)
    contactphone = models.CharField(db_column='ContactPhone', max_length=50, blank=True, null=True)
    contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True)
    director = models.IntegerField(db_column='Director', blank=True, null=True)
    createdt = models.DateTimeField(db_column='CreateDT', blank=True, null=True)
    updatedt = models.DateTimeField(db_column='UpdateDT', blank=True, null=True)
    tiebreakingurl = models.TextField(db_column='TieBreakingURL', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Organization'

    def __str__(self):
        return "{}".format(self.name)


class ScorbotSMSPhone(models.Model):
    smsid = models.AutoField(db_column='SMSID', primary_key=True)
    smsphoneid = models.IntegerField(db_column='SMSPhoneID', blank=True, null=True)
    smsphone = models.CharField(db_column='SMSPhone', max_length=50, blank=True, null=True)
    descrip = models.CharField(db_column='Descrip', max_length=200, blank=True, null=True)
    title = models.CharField(db_column='Title', max_length=100, blank=True, null=True)
    effectiveyear = models.IntegerField(db_column='EffectiveYear', blank=True, null=True)
    active = models.BooleanField(db_column='Active', blank=True, null=True)
    organizationid = models.ForeignKey(ScorbotOrganization, on_delete=models.SET_NULL,
                                       db_column='OrganizationID', blank=True, null=True, related_name='smsphones')

    class Meta:
        managed = False
        db_table = 'tbl_SMSPhones'

    def __str__(self):
        return self.smsid