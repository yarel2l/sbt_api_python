from django.db import models


class Facility(models.Model):
    # id = models.AutoField(db_column='ID')
    tournamentid = models.ForeignKey('tournaments.Tournament', on_delete=models.SET_NULL, null=True, blank=True,
                                     db_column='TournamentID', related_name='facilities')
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)
    zipcode = models.CharField(db_column='Zipcode', max_length=50, blank=True, null=True)
    director = models.CharField(db_column='Director', max_length=50, blank=True, null=True)
    cellphone = models.CharField(db_column='CellPhone', max_length=50, blank=True, null=True)
    director2 = models.CharField(db_column='Director2', max_length=50, blank=True, null=True)
    cellphone2 = models.CharField(db_column='CellPhone2', max_length=48)
    director3 = models.CharField(db_column='Director3', max_length=50, blank=True, null=True)
    cellphone3 = models.CharField(db_column='CellPhone3', max_length=48)
    active = models.IntegerField(db_column='Active', blank=True, null=True)
    getscores = models.IntegerField(db_column='GetScores', blank=True, null=True)
    position = models.IntegerField(db_column='Position')

    class Meta:
        managed = False
        db_table = 'tbl_Locations'
