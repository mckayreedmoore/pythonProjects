# Generated by Django 2.2.5 on 2021-06-22 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StarWarsUniverse', '0003_auto_20210622_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='Affiliation',
            field=models.CharField(choices=[('light', 'light'), ('dark', 'dark'), ('neutral', 'neutral')], default='neutral', max_length=60),
        ),
    ]