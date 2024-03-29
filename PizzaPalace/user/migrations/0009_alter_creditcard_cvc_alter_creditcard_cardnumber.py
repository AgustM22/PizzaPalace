# Generated by Django 4.2 on 2023-05-11 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_creditcard_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='CVC',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='CardNumber',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999999999)]),
        ),
    ]
