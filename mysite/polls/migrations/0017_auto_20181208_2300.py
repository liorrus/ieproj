# Generated by Django 2.1.3 on 2018-12-08 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20181208_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='porder',
            name='orderStatus',
            field=models.CharField(choices=[('W', 'WAITING'), ('R', 'READY'), ('T', 'TAKE')], default='WAITING', max_length=1),
        ),
    ]
