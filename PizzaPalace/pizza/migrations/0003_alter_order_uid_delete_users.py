# Generated by Django 4.2 on 2023-05-04 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('pizza', '0002_rename_price_product_pricelarge_offer_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='UID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.users'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]