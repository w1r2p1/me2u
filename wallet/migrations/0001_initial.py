# Generated by Django 2.1.2 on 2018-10-06 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exchange', '0005_auto_20181005_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='wallet name')),
                ('address', models.CharField(max_length=255, verbose_name='address')),
                ('crypto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exchange.Coin', verbose_name='Crypto currency')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
        ),
    ]
