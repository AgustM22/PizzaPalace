# Generated by Django 4.2 on 2023-05-06 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userprofile'),
        ('pizza', '0003_alter_order_uid_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='UID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile'),
        ),
    ]
