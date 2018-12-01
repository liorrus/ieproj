# Generated by Django 2.1.3 on 2018-12-01 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20181130_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdes', models.CharField(max_length=48)),
                ('slug', models.SlugField(default='STRING', max_length=40)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='product1',
        ),
    ]
