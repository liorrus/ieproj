# Generated by Django 2.1.3 on 2018-12-08 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_auto_20181208_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_price', models.FloatField(default=0.0)),
                ('extra_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Part')),
                ('extra_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Product')),
            ],
        ),
        migrations.RemoveField(
            model_name='extras',
            name='extra_part',
        ),
        migrations.RemoveField(
            model_name='extras',
            name='extra_product',
        ),
        migrations.AlterField(
            model_name='order',
            name='extra1',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='ex1', to='polls.MyExtra'),
        ),
        migrations.AlterField(
            model_name='order',
            name='extra2',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='ex2', to='polls.MyExtra'),
        ),
        migrations.AlterField(
            model_name='order',
            name='extra3',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='ex3', to='polls.MyExtra'),
        ),
        migrations.AlterField(
            model_name='order',
            name='extra4',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='ex4', to='polls.MyExtra'),
        ),
        migrations.AlterField(
            model_name='order',
            name='extra5',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='ex5', to='polls.MyExtra'),
        ),
        migrations.DeleteModel(
            name='Extras',
        ),
    ]
