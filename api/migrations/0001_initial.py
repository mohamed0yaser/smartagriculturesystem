# Generated by Django 4.1.9 on 2023-05-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Embedded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(max_length=255)),
                ('humidity', models.FloatField(max_length=255)),
                ('light', models.FloatField(max_length=255)),
                ('rainfall', models.FloatField(max_length=255)),
                ('soil_moisture', models.FloatField(max_length=255)),
            ],
        ),
    ]
