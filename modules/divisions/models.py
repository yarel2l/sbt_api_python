from django.db import models


class ScorbotDivision(models.Model):
    # id = models.AutoField(db_column='ID')
    tournamentid = models.ForeignKey('tournaments.Tournament', on_delete=models.SET_NULL,
                                     null=True, blank=True, db_column='TournamentID', related_name='divisions')
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)
    teamsperpool = models.IntegerField(db_column='TeamsPerPool', blank=True, null=True)
    perpooldesc = models.CharField(db_column='PerPoolDesc', max_length=50, blank=True, null=True)
    gamesperpool = models.IntegerField(db_column='GamesPerPool', blank=True, null=True)
    gppdesc = models.CharField(db_column='GPPDesc', max_length=50, blank=True, null=True)
    brackets = models.IntegerField(db_column='Brackets', blank=True, null=True)
    bracketsdesc = models.CharField(db_column='BracketsDesc', max_length=50, blank=True, null=True)
    minimumgames = models.IntegerField(db_column='MinimumGames', blank=True, null=True)
    divisiontype = models.CharField(db_column='DivisionType', max_length=10, blank=True, null=True)
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)
    gradeid = models.ForeignKey("core.ScorbotGrade", on_delete=models.SET_NULL, db_column='GradeID',
                                blank=True, null=True, related_name='divisions')
    sporttype = models.IntegerField(db_column='SportType', blank=True, null=True)
    hideschedule = models.IntegerField(db_column='HideSchedule', blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=50, blank=True, null=True)
    maincolor = models.CharField(db_column='MainColor', max_length=7, blank=True, null=True)
    altcolor = models.CharField(db_column='AltColor', max_length=7, blank=True, null=True)
    hometextcolor = models.CharField(db_column='HomeTextColor', max_length=7, blank=True, null=True)
    visitortextcolor = models.CharField(db_column='VisitorTextColor', max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Divisions'
