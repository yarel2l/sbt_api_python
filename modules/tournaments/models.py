from django.conf import settings
from django.db import models


class Tournament(models.Model):
    event_number = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)
    status = models.ForeignKey('core.ScorbotStatus', on_delete=models.SET_NULL, null=True, blank=True, db_column='Status')
    eventtype = models.ForeignKey('core.ScorbotEventType', on_delete=models.SET_NULL, db_column='EventType', blank=True, null=True)
    contactname = models.CharField(db_column='ContactName', max_length=50, blank=True, null=True)
    contactphone = models.CharField(db_column='ContactPhone', max_length=50, blank=True, null=True)
    getscores = models.IntegerField(db_column='GetScores', blank=True, null=True)
    contactname2 = models.CharField(db_column='ContactName2', max_length=50, blank=True, null=True)
    contactphone2 = models.CharField(db_column='ContactPhone2', max_length=50, blank=True, null=True)
    contactemail = models.CharField(db_column='ContactEmail', max_length=50, blank=True, null=True)
    website = models.CharField(db_column='Website', max_length=50, blank=True, null=True)
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)
    starttime = models.CharField(db_column='StartTime', max_length=8, blank=True, null=True)
    intervals = models.IntegerField(db_column='Intervals', blank=True, null=True)
    gameduration = models.IntegerField(db_column='GameDuration', blank=True, null=True)
    organization = models.ForeignKey('organizations.ScorbotOrganization', on_delete=models.SET_NULL,
                                     db_column='Organization', blank=True, null=True)
    maxpoints = models.IntegerField(db_column='MaxPoints')
    active = models.IntegerField(db_column='Active')
    timezone = models.ForeignKey('core.ScorbotTimezone', on_delete=models.SET_NULL,
                                 db_column='TimeZone', blank=True, null=True)
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)
    bracketstyle = models.IntegerField(db_column='BracketStyle', blank=True, null=True)
    # smsid = models.ForeignKey('organizations.ScorbotSMSPhone', on_delete=models.SET_NULL,
    #                           db_column='SMSID', blank=True, null=True)
    smsid = models.IntegerField(db_column='SMSID', blank=True, null=True)
    blocksms = models.IntegerField(db_column='BlockSMS', blank=True, null=True)
    robot = models.IntegerField(db_column='ROBOT', blank=True, null=True)
    divisiondesc = models.CharField(db_column='DivisionDesc', max_length=10, blank=True, null=True)
    genderdesc = models.CharField(db_column='GenderDesc', max_length=10, blank=True, null=True)
    multiregistrations = models.IntegerField(db_column='MultiRegistrations', blank=True, null=True)
    lastrelease = models.DateTimeField(db_column='LastRelease', blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)
    registrationpriceperteam = models.DecimalField(db_column='RegistrationPricePerTeam', max_digits=6, decimal_places=2)
    registrationfee = models.DecimalField(db_column='RegistrationFee', max_digits=6, decimal_places=2)
    registrationstartdate = models.DateTimeField(db_column='RegistrationStartDate')
    registrationenddate = models.DateTimeField(db_column='RegistrationEndDate')
    registrationcountteams = models.IntegerField(db_column='RegistrationCountTeams')
    registrationdiscount = models.DecimalField(db_column='RegistrationDiscount', max_digits=6, decimal_places=2,
                                               blank=True, null=True)

    def __str__(self):
        return "#{} - {}".format(self.event_number, self.name)

    class Meta:
        managed = False
        db_table = 'tbl_Tournaments'


class UserFavoriteTournament(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, db_column='UserID')
    tournamentid = models.ForeignKey('Tournament', on_delete=models.DO_NOTHING, db_column='TournamentID')

    class Meta:
        managed = False
        db_table = 'tbl_UsersFavouritesTournaments'


class TournamentUser(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    tournamentid = models.ForeignKey('Tournament', on_delete=models.SET_NULL, db_column='TournamentID',
                                     blank=True, null=True, related_name='tournament_users')
    userid = models.ForeignKey('users.ScorbotUser', on_delete=models.SET_NULL, db_column='UserID', blank=True, null=True)
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)
    isowner = models.BooleanField(db_column='IsOwner')

    class Meta:
        managed = False
        db_table = 'tbl_TournamentUsers'


class TournamentUserRole(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    tournamentusersid = models.ForeignKey('TournamentUser', on_delete=models.DO_NOTHING,
                                          db_column='TournamentUsersID')
    modulesid = models.ForeignKey('core.ScorbotModule', on_delete=models.SET_NULL,
                                  null=True, blank=True, db_column='ModulesID')
    access = models.CharField(db_column='Access', max_length=50)
    accesscode = models.IntegerField(db_column='AccessCode')
    updatedate = models.DateTimeField(db_column='UpdateDate')
    updateuser = models.CharField(db_column='UpdateUser', max_length=20)

    class Meta:
        managed = False
        db_table = 'tbl_TournamentUserRoles'


class TournamentUserInvitation(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    tournamentid = models.ForeignKey('Tournament', on_delete=models.DO_NOTHING, db_column='TournamentID',
                                     related_name="invitations")
    fromuserid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, db_column='FromUserID', related_name="invitations_sent")
    touserid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, db_column='ToUserID', blank=True, null=True, related_name="invitations_received")
    tophone = models.CharField(db_column='ToPhone', max_length=50)
    activationcode = models.CharField(db_column='ActivationCode', max_length=6, blank=True, null=True)
    status = models.ForeignKey('core.ScorbotStatus', on_delete=models.SET_NULL, null=True, blank=True, db_column='Status')
    createdt = models.DateTimeField(db_column='CreateDT')
    updatedt = models.DateTimeField(db_column='UpdateDT')

    class Meta:
        managed = False
        db_table = 'tbl_TournamentUserInvitations'


class TournamentInformation(models.Model):
    letterid = models.AutoField(db_column='LetterID', primary_key=True)
    tournamentid = models.OneToOneField(Tournament, on_delete=models.CASCADE, db_column='TournamentID',
                                        related_name="information")
    letter = models.TextField(db_column='Letter', blank=True, null=True)
    username = models.CharField(db_column='UserName', max_length=50, blank=True, null=True)
    flyerurl = models.URLField(db_column='FlyerURL', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_InfoLetter'


class TournamentLogo(models.Model):
    # id = models.IntegerField(db_column='ID', blank=True, null=True)
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Logos'