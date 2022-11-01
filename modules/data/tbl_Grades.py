# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblGrades(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    gradenbr = models.CharField(db_column='GradeNbr', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    byage = models.CharField(db_column='ByAge', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bygrade = models.CharField(db_column='ByGrade', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_Grades'
