from django.db import models


class Pool(models.Model):
    # id = models.AutoField(db_column='ID')
    tournamentid = models.ForeignKey('tournaments.Tournament', on_delete=models.SET_NULL, null=True, blank=True,
                                     db_column='TournamentID', related_name='pools')
    divisionid = models.ForeignKey('divisions.ScorbotDivision', on_delete=models.SET_NULL, null=True, blank=True,
                                   db_column='DivisionID', related_name='pools')
    poolname = models.CharField(db_column='PoolName', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Pools'


class PoolStandings(models.Model):
    # id = models.AutoField(db_column='ID')
    tournamentid = models.ForeignKey('tournaments.Tournament', on_delete=models.SET_NULL, null=True, blank=True,
                                     db_column='TournamentID', related_name='pool_standings')
    divisionid = models.ForeignKey('divisions.ScorbotDivision', on_delete=models.SET_NULL, null=True, blank=True,
                                   db_column='DivisionID', related_name='pool_standings')
    gamenbr = models.IntegerField(db_column='GameNbr', blank=True, null=True)
    playoffpoolid = models.IntegerField(db_column='PlayoffPoolID', blank=True, null=True)
    poolid = models.ForeignKey(Pool, on_delete=models.SET_NULL, db_column='PoolID', blank=True, null=True)
    poolname = models.CharField(db_column='PoolName', max_length=20, blank=True, null=True)
    teamid = models.IntegerField(db_column='TeamID', blank=True, null=True)
    teamname = models.CharField(db_column='TeamName', max_length=100, blank=True, null=True)
    win = models.IntegerField(db_column='Win', blank=True, null=True)
    lost = models.IntegerField(db_column='Lost', blank=True, null=True)
    setwin = models.IntegerField(db_column='SetWin', blank=True, null=True)
    setlost = models.IntegerField(db_column='SetLost', blank=True, null=True)
    setpct = models.FloatField(db_column='SetPCT', blank=True, null=True)
    tie = models.IntegerField(db_column='Tie', blank=True, null=True)
    pct = models.FloatField(db_column='PCT', blank=True, null=True)
    h2h_wl = models.CharField(db_column='H2H_WL', max_length=10, blank=True, null=True)
    h2h = models.FloatField(db_column='H2H', blank=True, null=True)
    pt = models.FloatField(db_column='PT', blank=True, null=True)
    pointsall = models.IntegerField(db_column='PointsAll', blank=True, null=True)
    pf = models.FloatField(db_column='PF', blank=True, null=True)
    pa = models.FloatField(db_column='PA', blank=True, null=True)
    credits = models.IntegerField(db_column='Credits', blank=True, null=True)
    debits = models.IntegerField(db_column='Debits', blank=True, null=True)
    pointstie2 = models.IntegerField(db_column='PointsTie2', blank=True, null=True)
    coin = models.IntegerField(db_column='Coin', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_PoolStandings'
