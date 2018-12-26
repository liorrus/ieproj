# Generated by Django 2.1.3 on 2018-12-08 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PartsInProduct',
            new_name='Pip',
        ),
        migrations.AddField(
            model_name='supplier',
            name='slug',
            field=models.SlugField(default='STRING'),
        ),
        migrations.AlterField(
            model_name='porderitem',
            name='porder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.POrder'),
        ),
    ]