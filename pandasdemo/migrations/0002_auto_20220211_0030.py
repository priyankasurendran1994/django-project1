# Generated by Django 3.2.12 on 2022-02-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandasdemo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=255, verbose_name='year')),
                ('sex', models.CharField(max_length=255, verbose_name='sex')),
                ('age_group', models.CharField(max_length=255, verbose_name='age_group')),
                ('Geographic_region_where_injury_occurred', models.CharField(max_length=255, verbose_name='Geographic_region_where_injury_occurred')),
                ('Employment_status', models.CharField(max_length=255, verbose_name='Employment_status')),
                ('Occupation', models.CharField(max_length=255, verbose_name='Occupation')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
