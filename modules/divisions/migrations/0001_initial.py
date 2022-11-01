# Generated by Django 3.2.16 on 2022-10-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScorbotDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('teamsperpool', models.IntegerField(blank=True, db_column='TeamsPerPool', null=True)),
                ('perpooldesc', models.CharField(blank=True, db_column='PerPoolDesc', max_length=50, null=True)),
                ('gamesperpool', models.IntegerField(blank=True, db_column='GamesPerPool', null=True)),
                ('gppdesc', models.CharField(blank=True, db_column='GPPDesc', max_length=50, null=True)),
                ('brackets', models.IntegerField(blank=True, db_column='Brackets', null=True)),
                ('bracketsdesc', models.CharField(blank=True, db_column='BracketsDesc', max_length=50, null=True)),
                ('minimumgames', models.IntegerField(blank=True, db_column='MinimumGames', null=True)),
                ('divisiontype', models.CharField(blank=True, db_column='DivisionType', max_length=10, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=10, null=True)),
                ('sporttype', models.IntegerField(blank=True, db_column='SportType', null=True)),
                ('hideschedule', models.IntegerField(blank=True, db_column='HideSchedule', null=True)),
                ('updatedate', models.DateTimeField(blank=True, db_column='UpdateDate', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='UpdateUser', max_length=50, null=True)),
                ('maincolor', models.CharField(blank=True, db_column='MainColor', max_length=7, null=True)),
                ('altcolor', models.CharField(blank=True, db_column='AltColor', max_length=7, null=True)),
                ('hometextcolor', models.CharField(blank=True, db_column='HomeTextColor', max_length=7, null=True)),
                ('visitortextcolor', models.CharField(blank=True, db_column='VisitorTextColor', max_length=7, null=True)),
            ],
            options={
                'db_table': 'tbl_Divisions',
                'managed': False,
            },
        ),
    ]
