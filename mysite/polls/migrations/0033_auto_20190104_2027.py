# Generated by Django 2.1.4 on 2019-01-04 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_auto_20190104_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderPick',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 4, 20, 27, 23, 17372)),
        ),
    ]