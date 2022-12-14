# Generated by Django 3.2.15 on 2022-09-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_alter_post_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Experimental', 'Experimental'), ('Folk/Country', 'Folk/Country'), ('Global', 'Global'), ('Jazz', 'Jazz'), ('Metal', 'Metal'), ('Pop/R&B', 'Pop/R&B'), ('Rap/Hip-Hop', 'Rap/Hip-Hop'), ('Rock', 'Rock'), ('Uncategorized', 'Uncategorized')], default='Uncategorized', max_length=255),
        ),
    ]
