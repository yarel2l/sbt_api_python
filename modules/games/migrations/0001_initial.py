# Generated by Django 3.2.16 on 2022-10-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameid', models.IntegerField(db_column='GameID')),
                ('slotid', models.IntegerField(blank=True, db_column='SlotID', null=True)),
                ('updflags', models.CharField(blank=True, db_column='UpdFlags', max_length=3, null=True)),
                ('bracketname', models.CharField(blank=True, db_column='BracketName', max_length=20, null=True)),
                ('bracketcanvas', models.CharField(db_column='BracketCanvas', max_length=10)),
                ('addline', models.CharField(blank=True, db_column='AddLine', max_length=1, null=True)),
                ('addlineu', models.CharField(blank=True, db_column='AddLineU', max_length=50, null=True)),
                ('addlined', models.CharField(blank=True, db_column='AddLineD', max_length=50, null=True)),
                ('startcolumn', models.IntegerField(blank=True, db_column='StartColumn', null=True)),
                ('bracketsection', models.IntegerField(blank=True, db_column='BracketSection', null=True)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=10, null=True)),
                ('gamenbr', models.IntegerField(blank=True, db_column='GameNbr', null=True)),
                ('hometeamid', models.IntegerField(blank=True, db_column='HomeTeamID', null=True)),
                ('hometeam', models.BinaryField(blank=True, db_column='HomeTeam', null=True)),
                ('hometype', models.CharField(blank=True, db_column='HomeType', max_length=1, null=True)),
                ('homepool', models.CharField(blank=True, db_column='HomePool', max_length=10, null=True)),
                ('homeseq', models.IntegerField(blank=True, db_column='HomeSeq', null=True)),
                ('homedefaultteam', models.CharField(blank=True, db_column='HomeDefaultTeam', max_length=100, null=True)),
                ('homename', models.CharField(blank=True, db_column='HomeName', max_length=100, null=True)),
                ('homescore', models.IntegerField(blank=True, db_column='HomeScore', null=True)),
                ('homewin', models.IntegerField(blank=True, db_column='HomeWin', null=True)),
                ('visitorteamid', models.IntegerField(blank=True, db_column='VisitorTeamID', null=True)),
                ('visitorteam', models.CharField(blank=True, db_column='VisitorTeam', max_length=50, null=True)),
                ('visitortype', models.CharField(blank=True, db_column='VisitorType', max_length=1, null=True)),
                ('visitorpool', models.CharField(blank=True, db_column='VisitorPool', max_length=10, null=True)),
                ('visitorseq', models.IntegerField(blank=True, db_column='VisitorSeq', null=True)),
                ('visitordefaultteam', models.CharField(blank=True, db_column='VisitorDefaultTeam', max_length=100, null=True)),
                ('visitorname', models.CharField(blank=True, db_column='VisitorName', max_length=100, null=True)),
                ('visitorscore', models.IntegerField(blank=True, db_column='VisitorScore', null=True)),
                ('visitorwin', models.IntegerField(blank=True, db_column='VisitorWin', null=True)),
                ('locationid', models.IntegerField(blank=True, db_column='LocationID', null=True)),
                ('gamedate', models.DateTimeField(blank=True, db_column='GameDate', null=True)),
                ('gametime', models.CharField(blank=True, db_column='GameTime', max_length=8, null=True)),
                ('timeid', models.IntegerField(blank=True, db_column='TimeID', null=True)),
                ('winner_hvt', models.CharField(blank=True, db_column='Winner_HVT', max_length=1, null=True)),
                ('playofflevel', models.CharField(blank=True, db_column='PlayoffLevel', max_length=5, null=True)),
                ('winnerplace', models.IntegerField(blank=True, db_column='WinnerPlace', null=True)),
                ('loserplace', models.IntegerField(blank=True, db_column='LoserPlace', null=True)),
                ('nextreminder', models.DateTimeField(blank=True, db_column='NextReminder', null=True)),
                ('prevreminder', models.IntegerField(blank=True, db_column='PrevReminder', null=True)),
                ('lastrelease', models.DateTimeField(blank=True, db_column='LastRelease', null=True)),
                ('updatedate', models.DateTimeField(blank=True, db_column='UpdateDate', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='UpdateUser', max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_Games',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GameSets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setnbr', models.IntegerField(blank=True, db_column='SetNbr', null=True)),
                ('homescore', models.IntegerField(blank=True, db_column='HomeScore', null=True)),
                ('visitorscore', models.IntegerField(blank=True, db_column='VisitorScore', null=True)),
                ('userid', models.CharField(blank=True, db_column='UserID', max_length=20, null=True)),
                ('updatedate', models.DateTimeField(blank=True, db_column='UpdateDate', null=True)),
            ],
            options={
                'db_table': 'tbl_GameSets',
                'managed': False,
            },
        ),
    ]
