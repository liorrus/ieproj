# Generated by Django 2.1.3 on 2018-12-08 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181208_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='components',
            name='pdes',
        ),
        migrations.RemoveField(
            model_name='extras',
            name='pdes',
        ),
        migrations.AddField(
            model_name='components',
            name='part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Part'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='components',
            name='quant',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='extras',
            name='part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Part'),
            preserve_default=False,
        ),
    ]