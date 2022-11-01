from django.conf import settings
from django.db import models

from core.constants import SCORBOT_GENDER_CHOICES


class Team(models.Model):
    teamid = models.AutoField(db_column='TeamID', primary_key=True)
    smsid = models.IntegerField(db_column='SMSID', blank=True, null=True)
    teamtxtid = models.IntegerField(db_column='TeamTxtID', blank=True, null=True)
    gradeid = models.IntegerField(db_column='GradeID', blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)
    coachname = models.CharField(db_column='CoachName', max_length=50, blank=True, null=True)
    coachphone = models.CharField(db_column='CoachPhone', max_length=50, blank=True, null=True)
    coachemail = models.CharField(db_column='CoachEmail', max_length=50, blank=True, null=True)
    assistantname = models.CharField(db_column='AssistantName', max_length=50, blank=True, null=True)
    assistantphone = models.CharField(db_column='AssistantPhone', max_length=50, blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)
    updatetid = models.IntegerField(db_column='UpdateTID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Teams'


class TeamCoach(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='UserID',
                               related_name="user_teams")
    gradeid = models.ForeignKey('core.ScorbotGrade', on_delete=models.SET_NULL, null=True, blank=True, db_column='GradeID')
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True,
                              choices=SCORBOT_GENDER_CHOICES)
    teamname = models.CharField(db_column='TeamName', max_length=50)
    coachname = models.CharField(db_column='CoachName', max_length=50, blank=True, null=True)
    coachphone = models.CharField(db_column='CoachPhone', max_length=50, blank=True, null=True)
    coachemail = models.CharField(db_column='CoachEmail', max_length=50, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)
    stateid = models.ForeignKey('states.ScorbotState', models.DO_NOTHING, db_column='StateID',
                                related_name="state_teams")
    createdt = models.DateTimeField(db_column='CreateDT')
    updatedt = models.DateTimeField(db_column='UpdateDT')
    ranktype = models.IntegerField(db_column='RankType', blank=True, null=True)
    mergedwith = models.IntegerField(db_column='MergedWith', blank=True, null=True)
    yboa_id = models.IntegerField(db_column='YBOA_ID', blank=True, null=True)

    def __str__(self):
        return self.teamname

    class Meta:
        managed = False
        db_table = 'tbl_TeamsCoach'


class TeamsCoachTournament(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    teamscoachid = models.ForeignKey(TeamCoach, models.DO_NOTHING, db_column='TeamsCoachID',
                                     related_name="teamscoach_tournaments")
    tournamentid = models.ForeignKey('tournaments.Tournament', models.DO_NOTHING, db_column='TournamentID',
                                     related_name="tournament_teams")
    smsid = models.ForeignKey('organizations.ScorbotSMSPhone', models.DO_NOTHING, db_column='SMSID',
                              related_name="sms_teams")
    teamtxtid = models.IntegerField(db_column='TeamTxtID')
    createdt = models.DateTimeField(db_column='CreateDT')

    class Meta:
        managed = False
        db_table = 'tbl_TeamsCoachTournaments'
        unique_together = (('smsid', 'teamtxtid'), ('teamscoachid', 'tournamentid'),)


class TeamInfo(models.Model):
    # id = models.AutoField(db_column='ID')
    tournamentid = models.IntegerField(db_column='TournamentID')
    divisionid = models.IntegerField(db_column='DivisionID')
    poolid = models.IntegerField(db_column='PoolID', blank=True, null=True)
    teamid = models.IntegerField(db_column='TeamID', blank=True, null=True)
    finals = models.IntegerField(db_column='Finals')
    teamnbr = models.IntegerField(db_column='TeamNbr', blank=True, null=True)
    getscores = models.IntegerField(db_column='GetScores', blank=True, null=True)
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)
    coachname = models.CharField(db_column='CoachName', max_length=50, blank=True, null=True)
    coachphone = models.CharField(db_column='CoachPhone', max_length=50, blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_TeamInfo'


class TeamInfoNew(models.Model):
    teaminfoid = models.AutoField(db_column='TeamInfoID', primary_key=True)
    tournamentid = models.ForeignKey("tournaments.Tournament", on_delete=models.SET_NULL,
                                     db_column='TournamentID', null=True, blank=True,
                                     related_name="tournament_teams_info")
    divisionid = models.ForeignKey("divisions.ScorbotDivision", on_delete=models.SET_NULL, db_column='DivisionID',
                                   null=True, blank=True, related_name="division_teams_divisions")
    poolid = models.ForeignKey("pools.Pool", on_delete=models.SET_NULL, db_column='PoolID', blank=True, null=True,
                               related_name="pool_teams")
    teamid = models.IntegerField(db_column='TeamID', blank=True, null=True)
    finals = models.IntegerField(db_column='Finals')
    ranking = models.IntegerField(db_column='Ranking', blank=True, null=True)
    teamtxtid = models.IntegerField(db_column='TeamTxtID', blank=True, null=True)
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)
    coachname = models.CharField(db_column='CoachName', max_length=50, blank=True, null=True)
    coachphone = models.CharField(db_column='CoachPhone', max_length=50, blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_TeamInfo_New'


class TeamPoints(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    teamid = models.IntegerField(db_column='TeamID', blank=True, null=True)
    tournamentid = models.IntegerField(db_column='TournamentID', blank=True, null=True)
    gameid = models.IntegerField(db_column='GameID', blank=True, null=True)
    pointsearned = models.IntegerField(db_column='PointsEarned', blank=True, null=True)
    games = models.IntegerField(db_column='Games', blank=True, null=True)
    wins = models.IntegerField(db_column='Wins', blank=True, null=True)
    isadded = models.BooleanField(db_column='IsAdded')

    class Meta:
        managed = False
        db_table = 'tbl_TeamPoints'


class TeamFans(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    tournamentid = models.IntegerField(db_column='TournamentID')
    smsid = models.IntegerField(db_column='SMSID', blank=True, null=True)
    teamtxtid = models.IntegerField(db_column='TeamTxtID', blank=True, null=True)
    teamid = models.IntegerField(db_column='TeamID')
    teaminfoid = models.IntegerField(db_column='TeamInfoID', blank=True, null=True)
    teamname = models.CharField(db_column='TeamName', max_length=50, blank=True, null=True)
    cellphone = models.CharField(db_column='CellPhone', max_length=11)
    updatedate = models.DateTimeField(db_column='UpdateDate')

    class Meta:
        managed = False
        db_table = 'tbl_TeamFans'