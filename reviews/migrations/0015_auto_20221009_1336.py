# Generated by Django 3.2.15 on 2022-10-09 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_rename_user_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
