# Generated by Django 3.0 on 2020-03-13 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_campingtrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='campitem',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.CampingTrip'),
            preserve_default=False,
        ),
    ]
