# Generated by Django 2.1.3 on 2018-11-19 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20181119_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='extra1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Extras'),
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('product', 'order', 'extra1')},
        ),
    ]