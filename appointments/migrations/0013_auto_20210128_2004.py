# Generated by Django 3.1.5 on 2021-01-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0012_auto_20210128_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('1', '09:00 – 10:00'), ('2', '10:00 – 11:00'), ('3', '11:00 – 12:00'), ('4', '12:00 – 13:00'), ('5', '13:00 – 14:00')], max_length=50),
        ),
    ]
