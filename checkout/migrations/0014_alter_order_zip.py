# Generated by Django 3.2.16 on 2022-12-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0013_alter_order_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='zip',
            field=models.IntegerField(default=0),
        ),
    ]
