from django.db import models


class Game(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    tournamentid = models.ForeignKey('tournaments.Tournament', on_delete=models.SET_NULL, null=True, blank=True,
                                     db_column='TournamentID', related_name='games')
    divisionid = models.ForeignKey('divisions.ScorbotDivision', on_delete=models.SET_NULL, null=True, blank=True,
                                   db_column='DivisionID', related_name='games')
    poolid = models.ForeignKey('pools.Pool', on_delete=models.SET_NULL, db_column='PoolID', blank=True, null=True,
                               related_name='games')
    gameid = models.IntegerField(db_column='GameID')
    slotid = models.IntegerField(db_column='SlotID', blank=True, null=True)
    updflags = models.CharField(db_column='UpdFlags', max_length=3, blank=True, null=True)
    bracketname = models.CharField(db_column='BracketName', max_length=20, blank=True, null=True)
    bracketcanvas = models.CharField(db_column='BracketCanvas', max_length=10)
    addline = models.CharField(db_column='AddLine', max_length=1, blank=True, null=True)
    addlineu = models.CharField(db_column='AddLineU', max_length=50, blank=True, null=True)
    addlined = models.CharField(db_column='AddLineD', max_length=50, blank=True, null=True)
    startcolumn = models.IntegerField(db_column='StartColumn', blank=True, null=True)
    bracketsection = models.IntegerField(db_column='BracketSection', blank=True, null=True)
    category = models.CharField(db_column='Category', max_length=10, blank=True, null=True)
    gamenbr = models.IntegerField(db_column='GameNbr', blank=True, null=True)
    hometeamid = models.IntegerField(db_column='HomeTeamID', blank=True, null=True)
    hometeam = models.BinaryField(db_column='HomeTeam', blank=True, null=True)
    hometype = models.CharField(db_column='HomeType', max_length=1, blank=True, null=True)
    homepool = models.CharField(db_column='HomePool', max_length=10, blank=True, null=True)
    homeseq = models.IntegerField(db_column='HomeSeq', blank=True, null=True)
    homedefaultteam = models.CharField(db_column='HomeDefaultTeam', max_length=100, blank=True, null=True)
    homename = models.CharField(db_column='HomeName', max_length=100, blank=True, null=True)
    homescore = models.IntegerField(db_column='HomeScore', blank=True, null=True)
    homewin = models.IntegerField(db_column='HomeWin', blank=True, null=True)
    visitorteamid = models.IntegerField(db_column='VisitorTeamID', blank=True, null=True)
    visitorteam = models.CharField(db_column='VisitorTeam', max_length=50, blank=True, null=True)
    visitortype = models.CharField(db_column='VisitorType', max_length=1, blank=True, null=True)
    visitorpool = models.CharField(db_column='VisitorPool', max_length=10, blank=True, null=True)
    visitorseq = models.IntegerField(db_column='VisitorSeq', blank=True, null=True)
    visitordefaultteam = models.CharField(db_column='VisitorDefaultTeam', max_length=100, blank=True, null=True)
    visitorname = models.CharField(db_column='VisitorName', max_length=100, blank=True, null=True)
    visitorscore = models.IntegerField(db_column='VisitorScore', blank=True, null=True)
    visitorwin = models.IntegerField(db_column='VisitorWin', blank=True, null=True)
    locationid = models.IntegerField(db_column='LocationID', blank=True, null=True)
    gamedate = models.DateTimeField(db_column='GameDate', blank=True, null=True)
    gametime = models.CharField(db_column='GameTime', max_length=8, blank=True, null=True)
    timeid = models.IntegerField(db_column='TimeID', blank=True, null=True)
    winner_hvt = models.CharField(db_column='Winner_HVT', max_length=1, blank=True, null=True)
    playofflevel = models.CharField(db_column='PlayoffLevel', max_length=5, blank=True, null=True)
    winnerplace = models.IntegerField(db_column='WinnerPlace', blank=True, null=True)
    loserplace = models.IntegerField(db_column='LoserPlace', blank=True, null=True)
    nextreminder = models.DateTimeField(db_column='NextReminder', blank=True, null=True)
    prevreminder = models.IntegerField(db_column='PrevReminder', blank=True, null=True)
    lastrelease = models.DateTimeField(db_column='LastRelease', blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Games'


class GameSets(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    tournamentid = models.ForeignKey('tournaments.Tournament', on_delete=models.SET_NULL,
                                     db_column='TournamentID', blank=True, null=True, related_name='gamesets')
    divisionid = models.ForeignKey('divisions.ScorbotDivision', on_delete=models.SET_NULL,
                                   db_column='DivisionID', blank=True, null=True, related_name='gamesets')
    poolid = models.ForeignKey('pools.Pool', on_delete=models.SET_NULL, db_column='PoolID', blank=True, null=True,
                               related_name='gamesets')
    gameid = models.ForeignKey(Game, on_delete=models.SET_NULL, db_column='GameID', blank=True, null=True,
                               related_name='gamesets')
    setnbr = models.IntegerField(db_column='SetNbr', blank=True, null=True)
    homescore = models.IntegerField(db_column='HomeScore', blank=True, null=True)
    visitorscore = models.IntegerField(db_column='VisitorScore', blank=True, null=True)
    userid = models.CharField(db_column='UserID', max_length=20, blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_GameSets'