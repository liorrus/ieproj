# Generated by Django 2.1.3 on 2018-12-08 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20181208_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extras',
            old_name='product',
            new_name='productExtra',
        ),
    ]
