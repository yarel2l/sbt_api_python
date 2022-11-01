from django.db import models


class ScorbotState(models.Model):
    # id = models.AutoField(db_column='ID', primary_key=True)
    state = models.CharField(db_column='State', max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_States'
