# Generated by Django 4.2 on 2023-05-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_users_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=255)),
                ('ProfilePic', models.CharField(max_length=9999)),
                ('StreetName', models.CharField(max_length=255)),
                ('HouseNumber', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('Country', models.CharField(max_length=255)),
                ('PostalCode', models.CharField(max_length=255)),
            ],
        ),
    ]
