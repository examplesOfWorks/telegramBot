# Generated by Django 3.2.9 on 2021-11-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgBot', '0004_auto_20211111_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(default=' ', unique=True, verbose_name='Внешний ID пользователя'),
        ),
    ]