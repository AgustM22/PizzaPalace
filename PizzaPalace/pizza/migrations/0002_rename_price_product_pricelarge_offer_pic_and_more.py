# Generated by Django 4.2 on 2023-05-03 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='pricelarge',
        ),
        migrations.AddField(
            model_name='offer',
            name='pic',
            field=models.CharField(default='0', max_length=9999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pic',
            field=models.CharField(default='0', max_length=9999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pricemedium',
            field=models.FloatField(default='1800'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pricesmall',
            field=models.FloatField(default='1800'),
            preserve_default=False,
        ),
    ]