# Generated by Django 2.2.5 on 2021-06-15 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SciFiWatchlist', '0006_auto_20210615_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Enjoyed',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Viewed',
        ),
    ]