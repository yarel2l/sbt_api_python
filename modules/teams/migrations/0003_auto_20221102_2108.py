# Generated by Django 3.2.16 on 2022-11-02 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_registrations'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.DeleteModel(
            name='TeamFans',
        ),
        migrations.DeleteModel(
            name='TeamInfo',
        ),
    ]