# Generated by Django 3.1.5 on 2021-01-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20210126_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
