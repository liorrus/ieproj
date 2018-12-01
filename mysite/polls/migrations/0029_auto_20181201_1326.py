# Generated by Django 2.1.3 on 2018-12-01 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_auto_20181201_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='component1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comp1', to='polls.Components'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='component2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comp2', to='polls.Components'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='component3',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comp3', to='polls.Components'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='component4',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comp4', to='polls.Components'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='component5',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comp5', to='polls.Components'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='extra1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ex1', to='polls.Extras'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='extra2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ex2', to='polls.Extras'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='extra3',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ex3', to='polls.Extras'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='extra4',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ex4', to='polls.Extras'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='extra5',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ex5', to='polls.Extras'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product1',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='pro1', to='polls.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product2',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='pro2', to='polls.Product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='product3',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='pro3', to='polls.Product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='extra1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex11', to='polls.Extras'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='extra2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex21', to='polls.Extras'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='extra3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex31', to='polls.Extras'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='extra4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex41', to='polls.Extras'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='extra5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ex51', to='polls.Extras'),
        ),
    ]
