# Generated by Django 4.1.7 on 2024-02-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities_Nairobi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
