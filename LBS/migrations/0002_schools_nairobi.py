# Generated by Django 5.0.2 on 2024-03-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LBS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools_Nairobi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=250)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
