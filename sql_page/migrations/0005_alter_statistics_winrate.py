# Generated by Django 3.2.19 on 2023-05-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql_page', '0004_auto_20230519_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistics',
            name='winrate',
            field=models.IntegerField(),
        ),
    ]