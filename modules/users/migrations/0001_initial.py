# Generated by Django 3.2.16 on 2022-10-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=255, null=True, unique=True)),
                ('active', models.BooleanField(db_column='Active')),
            ],
            options={
                'db_table': 'tbl_UsersMembership',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ScorbotUser',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('username', models.CharField(db_column='UserName', max_length=50, unique=True)),
                ('pword', models.CharField(blank=True, db_column='PWord', max_length=300, null=True)),
                ('textingphone', models.CharField(blank=True, db_column='TextingPhone', max_length=50, null=True)),
                ('utype', models.IntegerField(blank=True, db_column='UType', null=True)),
                ('lastupdate', models.DateTimeField(blank=True, db_column='LastUpdate', null=True)),
                ('activationcode', models.CharField(blank=True, db_column='ActivationCode', max_length=6, null=True)),
                ('active', models.BooleanField(blank=True, db_column='Active', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
                ('creationdate', models.DateTimeField(blank=True, db_column='CreationDate', null=True)),
            ],
            options={
                'db_table': 'tbl_Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('rollid', models.AutoField(db_column='RollID', primary_key=True, serialize=False)),
                ('access', models.CharField(blank=True, db_column='Access', max_length=50, null=True)),
                ('accesscode', models.IntegerField(blank=True, db_column='AccessCode', null=True)),
                ('updatedate', models.DateTimeField(blank=True, db_column='UpdateDate', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='UpdateUser', max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_UserRoles',
                'managed': False,
            },
        ),
    ]
