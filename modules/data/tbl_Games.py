# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblGames(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tournamentid = models.IntegerField(db_column='TournamentID')  # Field name made lowercase.
    divisionid = models.IntegerField(db_column='DivisionID')  # Field name made lowercase.
    poolid = models.IntegerField(db_column='PoolID', blank=True, null=True)  # Field name made lowercase.
    gameid = models.IntegerField(db_column='GameID')  # Field name made lowercase.
    slotid = models.IntegerField(db_column='SlotID', blank=True, null=True)  # Field name made lowercase.
    updflags = models.CharField(db_column='UpdFlags', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bracketname = models.CharField(db_column='BracketName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bracketcanvas = models.CharField(db_column='BracketCanvas', max_length=10)  # Field name made lowercase.
    addline = models.CharField(db_column='AddLine', max_length=1, blank=True, null=True)  # Field name made lowercase.
    addlineu = models.CharField(db_column='AddLineU', max_length=50, blank=True, null=True)  # Field name made lowercase.
    addlined = models.CharField(db_column='AddLineD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    startcolumn = models.IntegerField(db_column='StartColumn', blank=True, null=True)  # Field name made lowercase.
    bracketsection = models.IntegerField(db_column='BracketSection', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=10, blank=True, null=True)  # Field name made lowercase.
    gamenbr = models.IntegerField(db_column='GameNbr', blank=True, null=True)  # Field name made lowercase.
    hometeamid = models.IntegerField(db_column='HomeTeamID', blank=True, null=True)  # Field name made lowercase.
    hometeam = models.BinaryField(db_column='HomeTeam', blank=True, null=True)  # Field name made lowercase.
    hometype = models.CharField(db_column='HomeType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    homepool = models.CharField(db_column='HomePool', max_length=10, blank=True, null=True)  # Field name made lowercase.
    homeseq = models.IntegerField(db_column='HomeSeq', blank=True, null=True)  # Field name made lowercase.
    homedefaultteam = models.CharField(db_column='HomeDefaultTeam', max_length=100, blank=True, null=True)  # Field name made lowercase.
    homename = models.CharField(db_column='HomeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    homescore = models.IntegerField(db_column='HomeScore', blank=True, null=True)  # Field name made lowercase.
    homewin = models.IntegerField(db_column='HomeWin', blank=True, null=True)  # Field name made lowercase.
    visitorteamid = models.IntegerField(db_column='VisitorTeamID', blank=True, null=True)  # Field name made lowercase.
    visitorteam = models.CharField(db_column='VisitorTeam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    visitortype = models.CharField(db_column='VisitorType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    visitorpool = models.CharField(db_column='VisitorPool', max_length=10, blank=True, null=True)  # Field name made lowercase.
    visitorseq = models.IntegerField(db_column='VisitorSeq', blank=True, null=True)  # Field name made lowercase.
    visitordefaultteam = models.CharField(db_column='VisitorDefaultTeam', max_length=100, blank=True, null=True)  # Field name made lowercase.
    visitorname = models.CharField(db_column='VisitorName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    visitorscore = models.IntegerField(db_column='VisitorScore', blank=True, null=True)  # Field name made lowercase.
    visitorwin = models.IntegerField(db_column='VisitorWin', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.
    gamedate = models.DateTimeField(db_column='GameDate', blank=True, null=True)  # Field name made lowercase.
    gametime = models.CharField(db_column='GameTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    timeid = models.IntegerField(db_column='TimeID', blank=True, null=True)  # Field name made lowercase.
    winner_hvt = models.CharField(db_column='Winner_HVT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    playofflevel = models.CharField(db_column='PlayoffLevel', max_length=5, blank=True, null=True)  # Field name made lowercase.
    winnerplace = models.IntegerField(db_column='WinnerPlace', blank=True, null=True)  # Field name made lowercase.
    loserplace = models.IntegerField(db_column='LoserPlace', blank=True, null=True)  # Field name made lowercase.
    nextreminder = models.DateTimeField(db_column='NextReminder', blank=True, null=True)  # Field name made lowercase.
    prevreminder = models.IntegerField(db_column='PrevReminder', blank=True, null=True)  # Field name made lowercase.
    lastrelease = models.DateTimeField(db_column='LastRelease', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    updateuser = models.CharField(db_column='UpdateUser', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Games'
