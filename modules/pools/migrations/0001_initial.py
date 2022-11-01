# Generated by Django 3.2.16 on 2022-10-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poolname', models.CharField(blank=True, db_column='PoolName', max_length=50, null=True)),
            ],
            options={
                'db_table': 'tbl_Pools',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PoolStandings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamenbr', models.IntegerField(blank=True, db_column='GameNbr', null=True)),
                ('playoffpoolid', models.IntegerField(blank=True, db_column='PlayoffPoolID', null=True)),
                ('poolname', models.CharField(blank=True, db_column='PoolName', max_length=20, null=True)),
                ('teamid', models.IntegerField(blank=True, db_column='TeamID', null=True)),
                ('teamname', models.CharField(blank=True, db_column='TeamName', max_length=100, null=True)),
                ('win', models.IntegerField(blank=True, db_column='Win', null=True)),
                ('lost', models.IntegerField(blank=True, db_column='Lost', null=True)),
                ('setwin', models.IntegerField(blank=True, db_column='SetWin', null=True)),
                ('setlost', models.IntegerField(blank=True, db_column='SetLost', null=True)),
                ('setpct', models.FloatField(blank=True, db_column='SetPCT', null=True)),
                ('tie', models.IntegerField(blank=True, db_column='Tie', null=True)),
                ('pct', models.FloatField(blank=True, db_column='PCT', null=True)),
                ('h2h_wl', models.CharField(blank=True, db_column='H2H_WL', max_length=10, null=True)),
                ('h2h', models.FloatField(blank=True, db_column='H2H', null=True)),
                ('pt', models.FloatField(blank=True, db_column='PT', null=True)),
                ('pointsall', models.IntegerField(blank=True, db_column='PointsAll', null=True)),
                ('pf', models.FloatField(blank=True, db_column='PF', null=True)),
                ('pa', models.FloatField(blank=True, db_column='PA', null=True)),
                ('credits', models.IntegerField(blank=True, db_column='Credits', null=True)),
                ('debits', models.IntegerField(blank=True, db_column='Debits', null=True)),
                ('pointstie2', models.IntegerField(blank=True, db_column='PointsTie2', null=True)),
                ('coin', models.IntegerField(blank=True, db_column='Coin', null=True)),
            ],
            options={
                'db_table': 'tbl_PoolStandings',
                'managed': False,
            },
        ),
    ]