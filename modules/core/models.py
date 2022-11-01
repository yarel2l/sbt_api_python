from django.db import models


class ScorbotModule(models.Model):
    moduleid = models.IntegerField(db_column='ModuleID', primary_key=True)
    module = models.CharField(db_column='Module', max_length=50, blank=True, null=True)
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)
    updateuser = models.CharField(db_column='UpdateUser', max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Modules'


class ScorbotStatus(models.Model):
    statusid = models.AutoField(db_column='StatusID', primary_key=True)
    statusdesc = models.CharField(db_column='StatusDesc', max_length=50, blank=True, null=True)
    details = models.CharField(db_column='Details', max_length=255, blank=True, null=True)
    ranking = models.IntegerField(db_column='Ranking', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Status'


class ScorbotTimezone(models.Model):
    code = models.CharField(db_column='Code', max_length=5, blank=True, null=True)
    descrip = models.CharField(db_column='Descrip', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Zones'

    def __str__(self):
        return self.descrip


class ScorbotGrade(models.Model):
    # id = models.AutoField(db_column='ID')
    gradenbr = models.CharField(db_column='GradeNbr', max_length=2, blank=True, null=True)
    grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)
    byage = models.CharField(db_column='ByAge', max_length=10, blank=True, null=True)
    bygrade = models.CharField(db_column='ByGrade', max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Grades'


class ScorbotTime(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)
    desc = models.CharField(db_column='Desc', max_length=50, blank=True, null=True)
    minutes = models.IntegerField(db_column='Minutes', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_Time'


class ScorbotEventType(models.Model):
    # id = models.AutoField(db_column='ID')
    descr = models.CharField(db_column='Descr', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_EventType'