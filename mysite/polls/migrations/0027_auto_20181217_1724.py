# Generated by Django 2.1.3 on 2018-12-17 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_auto_20181217_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderPick',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 12, 17, 17, 24, 38, 17042)),
        ),
    ]
