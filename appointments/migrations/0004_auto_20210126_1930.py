# Generated by Django 3.1.5 on 2021-01-26 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20210126_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='availability',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appointments.calendar'),
        ),
    ]
