# Generated by Django 2.1.4 on 2019-01-04 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0033_auto_20190104_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderPick',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 1, 4, 20, 29, 40, 756052)),
        ),
    ]