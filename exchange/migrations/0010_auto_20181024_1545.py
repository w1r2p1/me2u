# Generated by Django 2.1.2 on 2018-10-24 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0009_trade_trade_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='trade_id',
            new_name='trade_uid',
        ),
    ]
