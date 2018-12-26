# Generated by Django 2.1.3 on 2018-12-08 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20181208_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extras',
            name='productExtra',
        ),
        migrations.AddField(
            model_name='extras',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Product'),
            preserve_default=False,
        ),
    ]