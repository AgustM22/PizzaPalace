# Generated by Django 4.2 on 2023-05-04 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
