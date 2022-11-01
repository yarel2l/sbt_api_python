# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblTournamenttiebreaker(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tournamentid = models.ForeignKey('TblTournaments', models.DO_NOTHING, db_column='TournamentID')  # Field name made lowercase.
    tiebreakerid = models.ForeignKey('TblTiebreaker', models.DO_NOTHING, db_column='TieBreakerID')  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserID')  # Field name made lowercase.
    createdt = models.DateTimeField(db_column='CreateDT')  # Field name made lowercase.
    updatedt = models.DateTimeField(db_column='UpdateDT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_TournamentTieBreaker'
