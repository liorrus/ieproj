# Generated by Django 2.1.3 on 2018-11-19 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20181118_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderPick',
            field=models.DateTimeField(),
        ),
    ]
