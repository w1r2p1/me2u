# Generated by Django 2.1.2 on 2018-10-16 12:34

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0005_auto_20181005_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='location',
            field=django_countries.fields.CountryField(max_length=2, verbose_name='location'),
        ),
    ]