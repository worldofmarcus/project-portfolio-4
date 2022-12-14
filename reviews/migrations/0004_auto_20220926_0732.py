# Generated by Django 3.2.15 on 2022-09-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220924_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.IntegerField(choices=[(0, 'Electronic'), (2, 'Folk/Country'), (3, 'Jazz'), (4, 'Pop/R&B'), (5, 'Rock'), (6, 'Experimental'), (7, 'Global'), (8, 'Metal'), (9, 'Rap/Hip-Hop'), (10, 'Uncategorized')], default=10),
        ),
    ]
