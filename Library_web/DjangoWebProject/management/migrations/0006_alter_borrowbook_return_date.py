# Generated by Django 4.2.20 on 2025-06-25 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_alter_borrowbook_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowbook',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 16, 15, 54, 46, 1415)),
        ),
    ]
