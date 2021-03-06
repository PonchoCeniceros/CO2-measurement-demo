# Generated by Django 3.2.3 on 2021-10-09 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('sensorId', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PPM', models.FloatField()),
                ('humidity', models.FloatField(null=True)),
                ('temperature', models.FloatField(null=True)),
                ('date', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.location')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.sensor')),
            ],
        ),
    ]
