# Generated by Django 2.1.3 on 2018-11-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20181119_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='extras',
            name='productExtra',
            field=models.ManyToManyField(to='polls.Product'),
        ),
    ]