# Generated by Django 3.2.9 on 2021-11-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgBot', '0003_auto_20211110_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
